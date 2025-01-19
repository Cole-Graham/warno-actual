# TODO-new-units.md

## Functions to migrate from old scripts
### new_units.py
- [x] new_units_deckserializer (DeckSerializer.ndf)
- ~~[ ] new_units_divisionpacks (DivisionPacks.ndf)~~ <sup>merged with unit edits</sup>
- ~~[ ] new_units_divisionrules (DivisionRules.ndf)~~ <sup>merged with unit edits</sup>
- ~~[ ] new_units_divisions (Divisions.ndf)~~ <sup>merged with unit edits</sup>
- ~~[ ] new_units_allunitstactic (AllUnitsTactic.ndf)~~ <sup>patched out by eugen</sup>
- ~~[ ] new_units_orderavailabilitytactic (OrderAvailability_Tactic.ndf)~~ <sup>merged</sup>
- [x] new_units_showroomunits (ShowroomUnits.ndf)
- ~~[ ] new_units_showroomequivalence (ShowroomEquivalence.ndf)~~ <sup>patched out by eugen</sup>
- [x] new_units_unitecadavredescriptor (UnitCadavreDescriptor.ndf)
- [x] new_units_depictionghosts (GeneratedDepictionGhosts.ndf)
- [x] new_units_depictionalternatives (DepictionAlternatives.ndf) <sup>using donor's models</sup>
- [x] new_units_depictionselectors (GeneratedDepictionSelectors.ndf)
- [x] new_units_depictionvehicles (GeneratedDepictionVehicles.ndf)
- [x] new_units_depictionhumans (GeneratedDepictionHumans.ndf)
- [x] new_units_depictionvehiclesshowroom (GeneratedDepictionVehiclesShowroom.ndf)
- [x] new_units_depictionaerialghosts (GeneratedDepictionAerialGhosts.ndf)
- [x] new_units_buttontexturesunites (ButtonTexturesUnites.ndf)
- [x] new_units_depictioninfantry (GeneratedDepictionInfantry.ndf)
- [x] new_units_weapondescriptor (WeaponDescriptor.ndf)
- [x] new_units_unitdescriptor (UniteDescriptor.ndf)

### UI_mods.py
#### Common Style
- [x] **edit_colors**                                                          
<sup>GameData/UserInterface/Style/Common/Colors.ndf</sup>
- [x] **edit_textstyles**                                                         
<sup>GameData/UserInterface/Style/Common/TextStyles.ndf</sup>

#### Default Style
- [x] **edit_defaultstyleguides**                                                 
<sup>GameData/UserInterface/Style/DefaultStyle/DefaultStyleGuides.ndf</sup>
- [x] **edit_defaulttextformatscript**                                           
<sup>GameData/UserInterface/Style/DefaultStyle/DefaultTextFormatScript.ndf</sup>

#### Common Templates
- [x] **edit_buckspecificbackgrounds**                                           
<sup>GameData/UserInterface/Use/Common/Templates/BuckSpecificBackgrounds.ndf</sup>
- [x] **edit_buckspecificbuttons**                                               
<sup>GameData/UserInterface/Use/Common/Templates/BuckSpecificButtons.ndf</sup>

#### Common Views
- [x] **edit_buckspecifichint**                                                   
<sup>GameData/UserInterface/Use/Common/Views/BUCKSpecificHint.ndf</sup>

#### Common UI
- [x] **edit_commontextures**                                                     
<sup>GameData/UserInterface/Use/Common/CommonTextures.ndf</sup>
- [x] **edit_uicommonflarelabelresources**                                        
<sup>GameData/UserInterface/Use/Common/UICommonFlareLabelResources.ndf</sup>
- [x] **edit_uispecificchatview**                                                 
<sup>GameData/UserInterface/Use/Common/UISpecificChatView.ndf</sup>
- [x] **edit_uispecificunitbuttonview**                                           
<sup>GameData/UserInterface/Use/Common/UISpecificUnitButtonView.ndf</sup>
- [x] **edit_uiwarningpanel**                                                     
<sup>GameData/UserInterface/Use/Common/UIWarningPanel.ndf</sup>

#### InGame UI
- [x] **edit_orderdisplay**                                                       
<sup>GameData/UserInterface/Use/InGame/OrderDisplay.ndf</sup>
- [x] **edit_uiingamebuckcubeaction**                                             
<sup>GameData/UserInterface/Use/InGame/UIInGameBUCKCubeAction.ndf</sup>
- [x] **edit_uiingamebuckengagementrules**                                        
<sup>GameData/UserInterface/Use/InGame/UIIngameBUCKEngagementRules.ndf</sup>
- [x] **edit_uiingamedefaultcontainer**                                            
<sup>GameData/UserInterface/Use/InGame/UIInGameDefaultContainer.ndf</sup>
- [x] **edit_uiingamehudreplayresource**                                          
<sup>GameData/UserInterface/Use/InGame/UIInGameHUDReplayResource.ndf</sup>
- [x] **edit_uiingamelaunchbattlebuttonresources**                                
<sup>GameData/UserInterface/Use/InGame/UIInGameLaunchBattleButtonResources.ndf</sup>
- [x] **edit_uiingameminimap**                                                    
<sup>GameData/UserInterface/Use/InGame/UIInGameMinimap.ndf</sup>
- [x] **edit_uiingameresources**                                                  
<sup>GameData/UserInterface/Use/InGame/UIInGameResources.ndf</sup>
- [x] **edit_uispecifichudalertpanelview**                                        
<sup>GameData/UserInterface/Use/InGame/UISpecificHUDAlertPanelView.ndf</sup>
- [x] **edit_uispecifichudmultiselectionpanelview**                               
<sup>GameData/UserInterface/Use/InGame/UISpecificHUDMultiSelectionPanelView.ndf</sup>
- [x] **edit_uispecifichudscoreview**                                             
<sup>GameData/UserInterface/Use/InGame/UISpecificHUDScoreView.ndf</sup>
- [x] **edit_uispecificingamehudtimepanelview**                                   
<sup>GameData/UserInterface/Use/InGame/UISpecificInGameHUDTimePanelView.ndf</sup>
- [x] **edit_uispecificingameidleunitview**                                       
<sup>GameData/UserInterface/Use/InGame/UISpecificInGameIdleUnitView.ndf</sup>
- [x] **edit_uispecificingameplayermissionlabelresources**                        
<sup>GameData/UserInterface/Use/InGame/UISpecificInGamePlayerMissionLabelResources.ndf</sup>
- [x] **edit_uispecificminimapinfoview**                                          
<sup>GameData/UserInterface/Use/InGame/UISpecificMiniMapInfoView.ndf</sup>
- [x] **edit_uispecificoffmapairplaneview**                                       
<sup>GameData/UserInterface/Use/InGame/UISpecificOffMapAirplaneView.ndf</sup>
- [x] **edit_uispecificoffmapview**                                               
<sup>GameData/UserInterface/Use/InGame/UISpecificOffMapView.ndf</sup>
- [x] **edit_uispecificshortcutsforselectionview**                                
<sup>GameData/UserInterface/Use/InGame/UISpecificShortcutsForSelectionView.ndf</sup>
- [x] **edit_uispecificskirmishproductionmenuview**                               
<sup>GameData/UserInterface/Use/InGame/UISpecificSkirmishProductionMenuView.ndf</sup>
- [x] **edit_uispecificunitlabelaggregationview**                                 
<sup>GameData/UserInterface/Use/InGame/UISpecificUnitLabelAggregationView.ndf</sup>
- [x] **edit_uispecificunitlabelcommon**                                          
<sup>GameData/UserInterface/Use/InGame/UISpecificUnitLabelCommon.ndf</sup>
- [x] **edit_uispecificunitlabelmultiselectionview**                              
<sup>GameData/UserInterface/Use/InGame/UISpecificUnitLabelMultiSelectionView.ndf</sup>
- [x] **edit_uispecificunitlabelview**                                            
<sup>GameData/UserInterface/Use/InGame/UISpecificUnitLabelView.ndf</sup>
- [x] **edit_uispecificunitlabelviewnameonly**                                    
<sup>GameData/UserInterface/Use/InGame/UISpecificUnitLabelViewNameOnly.ndf</sup>
- [x] **edit_uispecificunitselectionpanelview**                                   
<sup>GameData/UserInterface/Use/InGame/UISpecificUnitSelectionPanelView.ndf</sup>
- [x] **edit_uispecificunitselectionweaponpanelview**                             
<sup>GameData/UserInterface/Use/InGame/UISpecificUnitSelectionWeaponPanelView.ndf</sup>

#### OutGame UI
- [x] **edit_useoutgametextures**                                                 
<sup>GameData/UserInterface/Use/OutGame/UseOutGameTextures.ndf</sup>

#### ShowRoom UI
- [x] **edit_uispecificshowroomarmorycomponent**                                  
<sup>GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomArmoryComponent.ndf</sup>
- [x] **edit_uispecificshowroomdeckcreatorscreencomponent**                       
<sup>GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomDeckCreatorScreenComponent.ndf</sup>
- [x] **edit_uispecificshowroomgroupsdeckcreatorscreenview**                      
<sup>GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomGroupsDeckCreatorScreenView.ndf</sup>

#### Textures UI
- [x] **edit_minimapicons**                                                       
<sup>GameData/Generated/UserInterface/Textures/MinimapIcons.ndf</sup>
