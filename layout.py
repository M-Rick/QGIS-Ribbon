# -*- coding: utf-8 -*-
import os.path
import platform
import locale
import subprocess
import webbrowser
from qgis.utils import iface
import qgis
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QPushButton, QDockWidget, QVBoxLayout
from qgis.PyQt.QtWidgets import QPushButton, QStyleFactory
from qgis.PyQt.QtCore import QTranslator, QCoreApplication, QSize, \
    Qt, QRect, QPropertyAnimation, QEasingCurve, QSettings
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QToolBar, QToolButton, QWidget, \
    QHBoxLayout, QMenu, QMessageBox

# Initialize Qt resources from file resources.py
from qgis._core import QgsProject, Qgis, QgsSettings, QgsApplication
# from .resources import *
# Import the code for the dialog
# from .rib_layout_dialog import MainTabQgsWidgetDialog
from .config import Config
from .tools import StyleManager
from .utils import tr

from .dynamic_layout import Widget
from .ribbon_config import RIBBON_DEFAULT
from .CustomMessageBox import CustomMessageBox
project = QgsProject.instance()


class MainTabQgsWidget:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        self.install_translator()
        # initialize locale
        self.main_widget = Widget(self.iface.mainWindow())

        # list with hidden left docs, to reinstitute on user click
        self.left_docks = []
        # setup config structure for maintainning, toolbar and user interface
        # customization
        self.config = Config()
        #self.searcher = SearcherTool(self.main_widget, self.iface)

        # initialize StyleManager for styling handling
        self.style_manager = StyleManager(self)
        self.iface.initializationCompleted.connect(self.load_ribbons)
        self.iface.newProjectCreated.connect(self.missingCorePlugins)

    def missingCorePlugins(self):
        if len(iface.mainWindow().findChild(QToolBar, 'mVectorToolBar').actions()) == 0:
            CustomMessageBox(None, f'{tr("Switch on manually missing core plugin: Topology Checker")}').button_ok()

    def initGui(self):
        # set default style and active style if config.json doesn't extists
        dic_style = self.style_manager.get_style_dictionary()
        self.config.set_default_style(dic_style)

        style = self.main_widget.styleSheet()
        self.iface.mainWindow().statusBar().setStyleSheet(style + """
        QSpinBox {
            height: 20px;
        }
        """)
        self.save_default_user_layout()

        self.toolbar = QToolBar('RibToolBar', self.iface.mainWindow())
        self.toolbar.setObjectName('RibToolBar')
        self.iface.mainWindow().addToolBar(self.toolbar)
        self.toolbar.setMovable(False)
        self.toolbar.setFloatable(False)
        self.toolbar.addWidget(self.main_widget)

        self.menuButton = QToolButton()
        if platform.system() != 'Darwin':
            self.menuButton.setText(tr("Show menu"))
            self.menuButton.setCheckable(True)
            self.menuButton.setBaseSize(QSize(80, 25))
            self.menuButton.toggled.connect(self.menu_show)

        self.editButton = QToolButton()
        self.editButton.setText(tr("Edit menu"))
        self.editButton.setCheckable(True)
        self.editButton.setBaseSize(QSize(25, 25))
        self.editButton.toggled.connect(self.set_edit_session)
        self.menu_show()

        corner_widget = QWidget(self.main_widget.tabWidget)
        corner_layout = QHBoxLayout()
        corner_layout.setContentsMargins(0, 0, 0, 0)
        corner_layout.addWidget(self.menuButton)
        corner_layout.addWidget(self.editButton)

        corner_widget.setLayout(corner_layout)
        self.main_widget.tabWidget.setCornerWidget(corner_widget)
        self.iface.mapCanvas().refresh()

        # signals
        self.main_widget.editChanged.connect(self.save_user_ribbon_config)
        self.project_path = os.path.dirname(
            os.path.abspath(project.fileName()))
        self.toolbar.show()
        self.main_widget.setFocusPolicy(Qt.StrongFocus)

        process = qgis.utils.plugins.get('processing')
        if process:
            process.initGui()
            process.initProcessing()
            self.load_ribbons()

    def load_ribbons(self):
        # turn on ribbon editing
        self.main_widget.edit_session_toggle()

        ribbon_conf = self.config.load_user_ribbon_setup()
        if not ribbon_conf:
            ribbon_conf = RIBBON_DEFAULT

        for dtab in ribbon_conf:
            itab, tab = self.main_widget.add_tab(dtab['tab_name'])
            for dsec in dtab['sections']:
                sec = self.main_widget.add_section(
                    itab, tr(dsec['label']), dsec['btn_size']
                )
                for btn in dsec['btns']:
                    child = self.iface.mainWindow().findChild(QAction, btn[0])
                    if child is None:
                        sec.add_action(*btn)
                    else:
                        if btn[0] == 'mActionShowAlignRasterTool':
                            child.setIcon(QIcon(f'{self.plugin_dir}/icons/mActionShowAlignRasterTool.png'))
                        sec.add_action(child, *btn[1:])
                if dsec['label'] == 'Prints':
                    self.custom_prints()

        self.main_widget.tabWidget.setCurrentIndex(0)
        # turn off ribbon editing
        self.main_widget.edit_session_toggle()

    def visible_logo_rib_toolbar(self, visible):
        self.logo_toolbar.setVisible(not visible)

    def lock_logo_Toolbar(self):
        if not self.logo_toolbar.isVisible() and not self.toolbar.isVisible():
            self.logo_toolbar.setVisible(True)

    def off_on_search_tool(self, visibility):
        elements = ['comboBox_woj', 'comboBox_pow', 'comboBox_gmina', 'comboBox_obr',
                    'lineEdit_parcel', 'lineEdit_address', 'line']

        for elem in elements:
            getattr(self.main_widget, elem).setVisible(visibility)
        self.visibility_search_tool = not visibility

    def custom_prints(self):
        """Load custom tools to qgis"""

        b_mprints = self.main_widget.findChildren(QToolButton, 'ribMyPrints')
        for b_mprint in b_mprints:
            b_mprint.setIcon(QIcon(f'{self.plugin_dir}/icons/my_prints.png'))
        self.my_prints_setup()

    def save_default_user_layout(self):
        """ Saves active user toolbars in qgis user settings. Saves as string
        under flag org_toolbars in json config file (user scope).
        Assumes that all toolbars have specified name if not, we can't find
        them, and therefore will not be loaded again
        :return:
        """
        # select all active toolbars from mainwindow
        active_toolbars = []
        for x in self.iface.mainWindow().findChildren(QToolBar):
            try:
                if x.parent().windowTitle() == \
                        self.iface.mainWindow().windowTitle() and \
                        x.isVisible():
                    active_toolbars.append(x)
            except Exception:
                pass

        # hide toolbars
        for x in active_toolbars:
            x.hide()

        # unique and not empty objects name from toolbars
        tbars_names = [
            x.objectName() for x in active_toolbars
            if x.objectName() not in ['', None, 'NULL', 'RibToolBar']
        ]

        self.config.save_original_toolbars(tbars_names)

    def save_user_ribbon_config(self, opt):
        """Saves user ribbon setup to config on exit
        :opt: bool for edit session, False will save config
        :return: None
        """
        if not opt:
            conf = self.main_widget.generate_ribbon_config()
            self.config.save_user_ribbon_setup(conf)

    def load_default_user_layout(self):
        """Restores original user toolbars to qgis window from settings
        :return:
        """
        toolbars_name = self.config.get_original_toolbars()

        # find toolbars and swich their visiblity on
        for tname in toolbars_name:
            tbar = self.iface.mainWindow().findChild(QToolBar, tname)
            if tbar is not None:
                tbar.show()

        # show menu bar
        self.iface.mainWindow().menuBar().show()

    def my_prints_setup(self):
        btns = self.iface.mainWindow().findChildren(
            QToolButton, 'ribMyPrints')
        for btn in btns:
            btn.setToolTip(tr("My Prints"))
            btn.setPopupMode(QToolButton.InstantPopup)
            self.action_my_prints_menu()
            self.projectLayoutManager.layoutAdded.connect(
                self.action_my_prints_menu
            )
            self.projectLayoutManager.layoutRemoved.connect(
                self.action_my_prints_menu
            )

    def action_my_prints_menu(self):
        btns = self.iface.mainWindow().findChildren(
            QToolButton, 'ribMyPrints')
        for btn in btns:
            main_widget = self.main_widget
            menu = QMenu(main_widget)
            actions = []
            projectInstance = QgsProject.instance()
            self.projectLayoutManager = projectInstance.layoutManager()
            for layout in self.projectLayoutManager.layouts():
                title = layout.name()
                action = QAction(title, main_widget)
                action.triggered.connect(
                    lambda checked, item=action:
                    self.open_layout_by_name(item.text()))
                actions.append(action)
            actions.sort(key=lambda x: x.text())
            list(map(menu.addAction, actions))
            btn.setMenu(menu)

    def open_layout_by_name(self, action_name):
        layout = self.projectLayoutManager.layoutByName(action_name)
        self.iface.openLayoutDesigner(layout)

    def unload(self):
        self.iface.mainWindow().menuBar().show()
        self.style_manager.activate_style('')
        self.save_user_ribbon_config(False)
        # self.main_widget.unload_custom_actions()
        self.toolbar.hide()

        # reinstitute original qgis layout
        self.load_default_user_layout()

        self.iface.messageBar().pushMessage(
            'QGIS Ribbon',
            tr('Please, restart QGIS!'),
            Qgis.Info,
            0
        )

    def menu_show(self):
        """Toggle visiblity of menubar"""
        mbar = self.iface.mainWindow().menuBar()
        splitter_start = QRect(0, -20, mbar.width(), 20)
        splitter_end = QRect(0, 0, mbar.width(), 20)
        if self.menuButton.isChecked():
            mbar.show()
            self.set_animation(mbar, splitter_start, splitter_end, 200)
        else:
            self.set_animation(mbar, splitter_end, splitter_start, 200)
            mbar.hide()

    def set_edit_session(self):
        if self.editButton.isChecked():
            self.editButton.setText(tr("Finish edition"))
            self.main_widget.edit_session_toggle()
        else:
            self.editButton.setText(tr("Edit menu"))
            self.main_widget.edit_session_toggle(True)
            if self.main_widget.save == QMessageBox.No:
                for tabind in range(len(self.main_widget.tabs)):
                    self.main_widget.remove_tab(0)
                self.load_ribbons()

    def warstwy_show(self):
        splitter_start = QRect(-self.layer_panel.width(), self.layer_panel.y(),
                               self.layer_panel.width(), self.layer_panel.height())
        splitter_end = QRect(0, self.layer_panel.y(),
                             self.layer_panel.width(), self.layer_panel.height())
        if self.main_widget.pokaz_warstwy.isChecked():
            self.layer_panel.show()
            self.set_animation(self.layer_panel, splitter_start, splitter_end, 200)
            self.layer_view.resizeColumnToContents(0)
        else:
            self.set_animation(self.layer_panel, splitter_end, splitter_start, 200, 'out')

    def resize_layer_view(self):
        canvas_geom = self.iface.mapCanvas().geometry()
        self.layer_view.setGeometry(0, 79, 280, canvas_geom.height()-79)

    def set_animation(
            self, widget, qrect_start, qrect_end, duration, mode='in'):
        animation_in = QPropertyAnimation(widget, b"geometry")
        animation_in.setStartValue(qrect_start)
        animation_in.setEndValue(qrect_end)
        animation_in.setDuration(duration)
        animation_in.setEasingCurve(QEasingCurve.InOutQuad)
        animation_in.start()
        animation_in.finished.connect(
            lambda: self.delete_animation(animation_in, widget, mode)
        )

    def repair_layers_names_for_compositions(self):
        for layer in list(project.mapLayers().values()):
            layer.setName(layer.name().replace(':', '_'))

    def delete_animation(self, animation, widget, mode):
        del animation
        if mode == 'out': widget.hide()

    def restart_qgis(self):
        if project.write():
            res = CustomMessageBox(None, "The program must be restarted for the changes to take effect. Restart now?\n"
                                         "Aby zachować zmiany, program musi zostać uruchomiony ponownie. Czy uruchomić ponownie?").button_yes_no()
            if res == QMessageBox.Yes:
                project.setDirty(False)  # workaround - mimo poprawnego zapisu nadal pyta o zapis
                subprocess.Popen(f'{QgsApplication.arguments()[0]} {project.fileName()}')
                self.iface.actionExit().trigger()

    def install_translator(self):
        global locale
        locale = locale.setlocale(locale.LC_ALL, '')[0:2]
        try:
            # not always locale can be converted to str, apparently
            loc = str(QSettings().value('locale/userLocale'))
            if len(locale) > 1:
                locale = loc[:2]
        except Exception:
            # do not install translator -> english
            return
        if 'fr' in locale:
            trans_path = os.path.join(self.plugin_dir, 'i18n',
                                      f'rib_fr.qm')
        elif 'pl' in locale:
            trans_path = os.path.join(self.plugin_dir, 'i18n',
                                      f'rib_pl.qm')
        else:
            return
        if not os.path.exists(trans_path):
            return

        self.translator = QTranslator()
        self.translator.load(trans_path)
        QCoreApplication.installTranslator(self.translator)
