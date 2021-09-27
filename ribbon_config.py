from .utils import tr


RIBBON_DEFAULT = [
    {
        "tab_name": tr("Main Tools"),
        "tab_id": 'Main Tools',
        "sections": [
            
            {
                "label": tr("Project"),
                "btn_size": 30,
                "btns": [
                    ["mActionOpenProject", 0, 0],
                    ["mActionNewProject", 0, 1],
                    ["mActionSaveProject", 1, 0],
                    ["mActionSaveProjectAs", 1, 1],
                ]
            },
            
            {
                    'label': tr('Add Layer'),
                    'id': 'Add Layer',
                    'btn_size': 30,
                    'btns': [
                        ['mActionAddOgrLayer', 0, 0],
                        ['mActionAddWmsLayer', 0, 1],
                        ['mActionAddPgLayer', 0, 2],
                        ['mActionAddMeshLayer', 0, 3],
                        ['mActionAddWcsLayer', 0, 4],
                        ['mActionAddDelimitedText', 0, 5],
                        ['mActionAddMssqlLayer', 0, 6],
                        ['mActionAddDb2Layer', 1, 6],
                        ['mActionAddOracleLayer', 0, 7],
                        ['mActionAddRasterLayer', 1, 0],
                        ['mActionAddWfsLayer', 1, 1],
                        ['mActionAddSpatiaLiteLayer', 1, 2],
                        ['mActionAddVirtualLayer', 1, 3],
                        ['mActionAddAmsLayer', 1, 4],
                        ['mActionAddAfsLayer', 1, 5],
                        ['mActionDataSourceManager', 1, 6],
                    ],
                },
            
            {
                    'label': tr('Create Layer'),
                    'id': 'Create Layer',
                    'btn_size': 30,
                    'btns': [
                        ['mActionNewVectorLayer', 0, 0],
                        ['mActionNewMemoryLayer', 0, 1],
                        ['mActionNewVirtualLayer', 0, 2],
                        ['mActionNewGeoPackageLayer', 1, 0],
                        ['mActionNewSpatiaLiteLayer', 1, 1],
                        ['mActionTopologyChecker', 1, 2],
                    ],
            },
            
            {
                "label": tr("Navigation"),
                "btn_size": 30,
                "btns": [
                    ["mActionPan", 0, 0],
                    ["mActionZoomIn", 0, 1],
                    ["mActionZoomOut", 0, 2],
                    ["mActionZoomFullExtent", 0, 3],
                    ["mActionZoomActual", 0, 4],
                    ["mActionZoomToLayer", 1, 0],
                    ["mActionZoomToSelected", 1, 1],
                    ["mActionZoomLast", 1, 2],
                    ["mActionZoomNext", 1, 3],
                    ["mActionPanToSelected", 1, 4],
                ]
            },
            
            {
                'label': tr('Attributes'),
                'btn_size': 30,
                'btns': [
                    ['mActionIdentify', 0, 0],
                    ['mActionSelectFeatures', 0, 1],
                    ['mActionDeselectAll', 1, 0],
                    ['mActionOpenTable', 1, 1],
                ],
            },

            {
                'label': tr('Measurement'),
                'btn_size': 30,
                'btns': [
                    ['mActionMeasure', 0, 0],
                    ['mActionMeasureArea', 0, 1],
                    ['mActionMeasureAngle', 1, 0],
                ],
            },
            
            {
                    'label': tr('Prints'),
                    'id': 'Prints',
                    'btn_size': 30,
                    'btns': [
                        ['mActionNewPrintLayout', 0, 0],
                        ['mActionShowLayoutManager', 1, 0],
                        ['mActionNewReport', 0, 1],
                        ['mActionSaveMapAsPdf', 1, 1],
                ],
            },
            
            {
                    'label': tr('Decorations'),
                    'id': 'Decorations',
                    'btn_size': 30,
                    'btns': [
                        ['mActionDecorationGrid', 0, 0],
                        ['mActionDecorationImage', 0, 1],
                        ['mActionDecorationTitle', 0, 2],
                        ['mActionDecorationCopyright', 0, 3],
                        ['mActionDecorationLayoutExtent', 1, 0],
                        ['mActionDecorationScaleBar', 1, 1],
                        ['mActionDecorationNorthArrow', 1, 2],
                ]
            },
            
            {
                    'label': tr('Settings'),
                    'id': 'Database',
                    'btn_size': 30,
                    'btns': [
                        ['mActionOptions', 0, 0],
                        ['mActionStyleManager', 0, 1],
                        ['mActionCustomProjection', 0, 2],
                        ['mActionHelpContents', 0, 3],
                        ['mActionCustomization', 1, 0],
                        ['mActionConfigureShortcuts', 1, 1],
                        ['mActionShowPythonDialog', 1, 2],
                        ['mActionManagePlugins', 1, 3],
                ]
            },
            
            {
                    'label': tr(' '),
                    'id': 'About',
                    'btn_size': 80,
                    'btns': [
                        [' ', 0, 0],
                        [' ', 0, 1],
                        ['mActionAbout', 0, 2],
                ]
            },
            
        ]
    },

    {
        "tab_name": tr("Advanced Tools"),
        "tab_id": "Advanced Tools",
        "sections": [
            
            {
                'label': tr('Selection'),
                'id': 'Selection',
                'btn_size': 30,
                'btns': [
                    ['mActionSelectFeatures', 0, 0],
                    ['mActionSelectPolygon', 0, 1],
                    ['mActionSelectByExpression', 0, 3],
                    ['mActionSelectByForm', 0, 4],
                    ['mActionDeselectAll', 0, 5],
                    ['mActionDeselectActiveLayer', 0, 6],
                    ['mActionSelectFreehand', 1, 0],
                    ['mActionSelectRadius', 1, 1],
                    ['mActionSelectAll', 1, 2],
                    ['mActionInvertSelection', 1, 3],
                    ['mProcessingAlg_native:selectbylocation', 1, 4],
                    ['mActionReselect', 1, 5],
                ],
            },
            
            {
                'label': tr('Advanced attributes'),
                'btn_size': 30,
                'btns': [
                    ['mActionIdentify', 0, 0],
                    ['mActionOpenTable', 0, 1],
                    ['mActionOpenFieldCalc', 0, 2],
                    ['mActionNewBookmark', 0, 3],
                    ['mActionShowBookmarks', 0, 4],
                    ['mActionMapTips', 0, 5],
                    ['mActionSnappingOptions', 0, 6],
                    ['mActionTextAnnotation', 0, 7],
                    
                    ['mActionDraw', 1, 0],
                    ['mActionTemporalController', 1, 1],
                    ['mActionStatisticalSummary', 1, 2],
                    ['mActionNewMapCanvas', 1, 3],
                    ['mActionNew3DMapCanvas', 1, 4],
                ],
            },
            
            {
                'label': tr('Vector'),
                'btn_size': 30,
                'btns': [
                    ['mActionToggleEditing', 0, 0],
                    ['mActionSaveLayerEdits', 0, 1],
                    ['mActionAllEdits', 0, 2],
                    ['mActionUndo', 0, 3],
                    ['mActionRedo', 0, 4],
                    ['mActionMultiEditAttributes', 1, 0],
                    ['mActionCutFeatures', 1, 1],
                    ['mActionCopyFeatures', 1, 2],
                    ['mActionPasteFeatures', 1, 3],
                    ['mActionDeleteSelected', 1, 4],
                ],
            },
            
            {
                'label': tr('Digitizing'),
                'btn_size': 30,
                'btns': [
                    ['EnableSnappingAction', 0, 0],
                    ['mActionAddFeature', 0, 1],
                    ['mActionMoveFeature', 0, 2],
                    ['mActionMoveFeatureCopy', 0, 3],
                    ['mActionRotateFeature', 0, 4],
                    ['mActionSplitFeatures', 0, 5],
                    ['mActionSplitParts', 0, 6],
                    ['mActionOffsetCurve', 0, 7],
                    ['mActionCircularStringCurvePoint', 0, 8],
                    ['mActionCircle2Points', 0, 9],
                    ['mActionCircle3Points', 0, 10],
                    ['mActionCircleCenterPoint', 0, 11],
                    ['mActionEllipseCenter2Points', 0, 12],
                    ['mActionEllipseCenterPoint', 0, 13],
                    ['mActionRectangleExtent', 0, 14],
                    ['mActionRectangleCenterPoint', 0, 15],
                    ['mActionRegularPolygon2Points', 0, 16],
                    ['mActionRegularPolygonCenterPoint', 0, 17],
                    ['mActionAddRing', 0, 18],
                    ['mActionAddPart', 0, 19],
                    ['mActionFillRing', 0, 20],
                    ['EnableTracingAction', 1, 0],
                    ['mActionVertexToolActiveLayer', 1, 1],
                    ['mActionVertexTool', 1, 2],
                    ['mActionReverseLine', 1, 3],
                    ['mActionTrimExtendFeature', 1, 4],
                    ['mActionMergeFeatures', 1, 5],
                    ['mActionMergeFeatureAttributes', 1, 6],
                    ['mActionSimplifyFeature', 1, 7],
                    ['mActionCircularStringRadius', 1, 8],
                    ['mActionCircle3Tangents', 1, 9],
                    ['mActionCircle2TangentsPoint', 1, 10],
                    [' ', 1, 11],
                    ['mActionEllipseExtent', 1, 12],
                    ['mActionEllipseFoci', 1, 13],
                    ['mActionRectangle3PointsDistance', 1, 14],
                    ['mActionRectangle3PointsProjected', 1, 15],
                    ['mActionRegularPolygonCenterPoint', 1, 16],
                    [' ', 1, 17],
                    ['mActionDeleteRing', 1, 18],
                    ['mActionDeletePart', 1, 19],
                    ['mActionReshapeFeatures', 1, 20],
                ]
            },
            
            {
                'label': tr('Labels'),
                'btn_size': 30,
                'btns': [
                    ['mActionLabeling', 0, 0],
                    ['mActionChangeLabelProperties', 0, 1],
                    ['mActionPinLabels', 0, 2],
                    ['mActionShowPinnedLabels', 0, 3],
                    ['mActionShowHideLabels', 0, 4],
                    ['mActionMoveLabel', 1, 0],
                    ['mActionRotateLabel', 1, 1],
                    ['mActionDiagramProperties', 1, 2],
                    ['mActionShowUnplacedLabels', 1, 3],
                ]
            },
           
        ]
    },
    
    {
        "tab_name": tr("Vector"),
        "tab_id": "Vector",
        "sections": [
            {
                'label': tr('Geoprocessing Tools'),
                'id': 'Geoprocessing Tools',
                'btn_size': 30,
                'btns': [
                    ['mProcessingUserMenu_native:buffer', 0, 0],
                    ['mProcessingUserMenu_native:clip', 1, 0],
                    ['mProcessingUserMenu_native:convexhull', 0, 1],
                    ['mProcessingUserMenu_native:difference', 0, 2],
                    ['mProcessingUserMenu_native:dissolve', 0, 3],
                    ['mProcessingUserMenu_native:intersection', 1, 1],
                    ['mProcessingUserMenu_native:symmetricaldifference', 1, 2],
                    ['mProcessingUserMenu_native:union', 1, 3],
                    ['mProcessingUserMenu_qgis:eliminateselectedpolygons', 0, 4],
                ]
            },
            
            {
                'label': tr('Geometry Tools'),
                'id': 'Geometry Tools',
                'btn_size': 30,
                'btns': [
                    ['mProcessingUserMenu_native:centroids', 0, 0],
                    ['mProcessingUserMenu_native:collect', 0, 1],
                    ['mProcessingUserMenu_native:densifygeometries', 0, 2],
                    ['mProcessingUserMenu_native:extractvertices', 0, 3],
                    ['mProcessingUserMenu_native:multiparttosingleparts', 0, 4],
                    ['mProcessingUserMenu_native:polygonstolines', 0, 5],
                    ['mProcessingUserMenu_native:simplifygeometries', 1, 0],
                    ['mProcessingUserMenu_qgis:checkvalidity', 1, 1],
                    ['mProcessingUserMenu_qgis:delaunaytriangulation', 1, 2],
                    ['mProcessingUserMenu_qgis:exportaddgeometrycolumns', 1, 3],
                    ['mProcessingUserMenu_qgis:linestopolygons', 1, 4],
                    ['mProcessingUserMenu_qgis:voronoipolygons', 1, 5],
                ],
            },

            {
               'label': tr('Analysis Tools'),
               'id': 'Analysis Tools',
               'btn_size': 30,
               'btns': [
                   ['mProcessingUserMenu_native:countpointsinpolygon', 0, 0],
                   ['mProcessingUserMenu_native:lineintersections', 0, 1],
                   ['mProcessingUserMenu_native:meancoordinates', 0, 2],
                   ['mProcessingUserMenu_native:nearestneighbouranalysis', 0, 3],
                   ['mProcessingUserMenu_native:sumlinelengths', 1, 0],
                   ['mProcessingUserMenu_qgis:basicstatisticsforfields', 1, 1],
                   ['mProcessingUserMenu_qgis:distancematrix', 1, 2],
                   ['mProcessingUserMenu_qgis:listuniquevalues', 1, 3],
               ],
           },

            {
               'label': tr('Research Tools'),
               'id': 'Research Tools',
               'btn_size': 30,
               'btns': [
                   ['mProcessingUserMenu_native:creategrid', 0, 0],
                   ['mProcessingUserMenu_native:polygonfromlayerextent', 0, 1],
                   ['mProcessingUserMenu_native:randompointsinextent', 0, 2],
                   ['mProcessingUserMenu_native:randompointsinpolygons', 0, 3],
                   ['mProcessingUserMenu_native:randompointsonlines', 0, 4],
                   ['mProcessingUserMenu_native:selectbylocation', 0, 5],
                   ['mProcessingUserMenu_qgis:randompointsinlayerbounds', 1, 0],
                   ['mProcessingUserMenu_qgis:randompointsinsidepolygons', 1, 1],
                   ['mProcessingUserMenu_qgis:randomselection', 1, 2],
                   ['mProcessingUserMenu_qgis:randomselectionwithinsubsets', 1, 3],
                   ['mProcessingUserMenu_qgis:regularpoints', 1, 4],
               ],
           },

            {
               'label': tr('Data Management Tools'),
               'id': 'Data Management Tools',
               'btn_size': 30,
               'btns': [
                   ['mProcessingUserMenu_native:createspatialindex', 0, 0],
                   ['mProcessingUserMenu_native:joinattributesbylocation', 0, 1],
                   ['mProcessingUserMenu_native:mergevectorlayers', 0, 2],
                   ['mProcessingUserMenu_native:reprojectlayer', 1, 0],
                   ['mProcessingUserMenu_native:splitvectorlayer', 1, 1],
               ],
           },

        ]
    },

    {
        "tab_name": tr("Raster"),
        "tab_id": "Raster",
        "sections": [
            {
                'label': tr('Raster'),
                'id': 'Raster',
                'btn_size': 60,
                'btns': [
                    ['mActionShowRasterCalculator', 0, 0],
                    ['mActionShowGeoreferencer', 0, 1],
                    ['mActionShowAlignRasterTool', 0, 2],
                ],
            },

            {
                'label': tr('Raster analysis'),
                'id': 'Raster analysis',
                'btn_size': 30,
                'btns': [
                    ['mProcessingUserMenu_gdal:aspect', 0, 0],
                    ['mProcessingUserMenu_gdal:fillnodata', 0, 1],
                    ['mProcessingUserMenu_gdal:gridaverage', 0, 2],
                    ['mProcessingUserMenu_gdal:griddatametrics', 0, 3],
                    ['mProcessingUserMenu_gdal:gridinversedistance', 0, 4],
                    ['mProcessingUserMenu_gdal:gridnearestneighbor', 0, 5],
                    ['mProcessingUserMenu_gdal:hillshade', 0, 6],
                    ['mProcessingUserMenu_gdal:nearblack', 1, 0],
                    ['mProcessingUserMenu_gdal:proximity', 1, 1],
                    ['mProcessingUserMenu_gdal:roughness', 1, 2],
                    ['mProcessingUserMenu_gdal:sieve', 1, 3],
                    ['mProcessingUserMenu_gdal:slope', 1, 4],
                    ['mProcessingUserMenu_gdal:tpitopographicpositionindex', 1, 5],
                    ['mProcessingUserMenu_gdal:triterrainruggednessindex', 1, 6],
                ],
            },

            {
                'label': tr('Projections'),
                'id': 'Projections',
                'btn_size': 60,
                'btns': [
                    ['mProcessingUserMenu_gdal:warpreproject', 0, 0],
                    ['mProcessingUserMenu_gdal:assignprojection', 0, 1],
                    ['mProcessingUserMenu_gdal:extractprojection', 0, 2],
                ],
            },

            {
                'label': tr('Miscellaneous'),
                'id': 'Miscellaneous',
                'btn_size': 30,
                'btns': [
                    ['mProcessingUserMenu_gdal:buildvirtualraster', 0, 0],
                    ['mProcessingUserMenu_gdal:gdalinfo', 0, 1],
                    ['mProcessingUserMenu_gdal:merge', 0, 2],
                    ['mProcessingUserMenu_gdal:overviews', 1, 0],
                    ['mProcessingUserMenu_gdal:tileindex', 1, 1],
                ],
            },

            {
                'label': tr('Extract Projection'),
                'id': 'Extract Projection',
                'btn_size': 30,
                'btns': [
                    ['mProcessingUserMenu_gdal:cliprasterbyextent', 0, 0],
                    ['mProcessingUserMenu_gdal:cliprasterbymasklayer', 0, 1],
                    ['mProcessingUserMenu_gdal:contour', 1, 0],
                ],
            },

            {
               'label': tr('Conversion'),
               'id': 'Conversion',
               'btn_size': 30,
               'btns': [
                   ['mProcessingUserMenu_gdal:pcttorgb', 0, 0],
                   ['mProcessingUserMenu_gdal:rgbtopct', 0, 1],
                   ['mProcessingUserMenu_gdal:polygonize', 0, 2],
                   ['mProcessingUserMenu_gdal:rasterize', 1, 0],
                   ['mProcessingUserMenu_gdal:translate', 1, 1],
               ],
           },
        ]
    },

]
