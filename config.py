import os

# Relative paths (best for portability)

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets the script's directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MASTER_DATASET_FILE = os.path.join(BASE_DIR,"dataset","centralizedMasterDB")  # Change this only when needed
#TEST_DATASET_FILE = os.path.join(BASE_DIR,"dataset","Cntralzd_TestOccupInGT")

#Occupant ID file
OCCUPANT_IDS_INIT = os.path.join(BASE_DIR,"dataset","occupantNameIDIndex.csv") #Need to be used when all occupants are considered
#Intermediate Name file_exists
#INTER_NAMEFILE = os.path.join(BASE_DIR,"dataset","inter_names.csv")
#OCCUPANT_IDS  = os.path.join(BASE_DIR,"dataset","inter_names.csv")

#Building/Zone ID fieldnames
#ZONE_IDS = os.path.join(BASE_DIR,"dataset","zoneList_mixed.csv") #Actual Zone list with all zones
ZONE_IDS = os.path.join(BASE_DIR,"dataset","zoneList_mixed.csv")

BUILDING_IDS = os.path.join(BASE_DIR,"dataset","buildingIDs.csv")
#Encodngs
MASTER_ENCODINGS = os.path.join(BASE_DIR,"encodings","21rmvd_train_crop_Encodings.pickle")
TEST_ENCODINGS = os.path.join(BASE_DIR,"encodings","21rmvd_test_crop_Encodings.pickle")



#Occupant Index list to ensure unique image for eah event
OCCUPANT_INDEX_LIST_FOREACHBUILD = os.path.join(BASE_DIR,"dataset","random_indexperFullGT.pickle")
OCCUPANT_INDEX_LIST_FOREACHBUILD_BACKUP = os.path.join(BASE_DIR,"dataset","random_indexperFullGT_backup.pickle")

#Event : Key Value Encodings
EVENT_KEYVALUE_CSTS = os.path.join(BASE_DIR,"dataset","Cntralzd_keyUsrValEncod.pickle")
INTER_EVENT_KEYVALUE_CSTS = os.path.join(BASE_DIR,"dataset","inter_Cntralzd_keyUsrValEncod.pickle")

#Valid and invalid TrackS
VALID_INVALID_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","estimated_validTrack.csv")

#========================================================Encodings : Building Specific =======================================
B1_REG_ENCODINGS = os.path.join(BASE_DIR,"encodings","b1_DataEncodings.pickle")
B1_VISIT_ENCODINGS = os.path.join(BASE_DIR,"encodings","b1_VisitorEncodings.pickle")
#------
B2_REG_ENCODINGS = os.path.join(BASE_DIR,"encodings","b2_DataEncodings.pickle")
B2_VISIT_ENCODINGS = os.path.join(BASE_DIR,"encodings","b2_VisitorEncodings.pickle")
#-----
B3_REG_ENCODINGS = os.path.join(BASE_DIR,"encodings","b3_DataEncodings.pickle")
B3_VISIT_ENCODINGS = os.path.join(BASE_DIR,"encodings","b3_VisitorEncodings.pickle")
#------
B4_REG_ENCODINGS = os.path.join(BASE_DIR,"encodings","b4_DataEncodings.pickle")
B4_VISIT_ENCODINGS = os.path.join(BASE_DIR,"encodings","b4_VisitorEncodings.pickle")
#-----
B5_REG_ENCODINGS = os.path.join(BASE_DIR,"encodings","b5_DataEncodings.pickle")
B5_VISIT_ENCODINGS = os.path.join(BASE_DIR,"encodings","b5_VisitorEncodings.pickle")
#------
B6_REG_ENCODINGS = os.path.join(BASE_DIR,"encodings","b6_DataEncodings.pickle")
B6_VISIT_ENCODINGS = os.path.join(BASE_DIR,"encodings","b6_VisitorEncodings.pickle")
#-----
B7_REG_ENCODINGS = os.path.join(BASE_DIR,"encodings","b7_DataEncodings.pickle")
B7_VISIT_ENCODINGS = os.path.join(BASE_DIR,"encodings","b7_VisitorEncodings.pickle")
#------
B8_REG_ENCODINGS = os.path.join(BASE_DIR,"encodings","b8_DataEncodings.pickle")
B8_VISIT_ENCODINGS = os.path.join(BASE_DIR,"encodings","b8_VisitorEncodings.pickle")
#-----
B9_REG_ENCODINGS = os.path.join(BASE_DIR,"encodings","b9_DataEncodings.pickle")
B9_VISIT_ENCODINGS = os.path.join(BASE_DIR,"encodings","b9_VisitorEncodings.pickle")
#------
B10_REG_ENCODINGS = os.path.join(BASE_DIR,"encodings","b10_DataEncodings.pickle")
B10_VISIT_ENCODINGS = os.path.join(BASE_DIR,"encodings","b10_VisitorEncodings.pickle")
#========================================================Distance Threshold : Building Specific ==============================
B1_DISTANCE_THRESH = os.path.join(BASE_DIR,"distance_threshold","b1_distanceThreshold.csv")
B2_DISTANCE_THRESH = os.path.join(BASE_DIR,"distance_threshold","b2_distanceThreshold.csv")
B3_DISTANCE_THRESH = os.path.join(BASE_DIR,"distance_threshold","b3_distanceThreshold.csv")
B4_DISTANCE_THRESH = os.path.join(BASE_DIR,"distance_threshold","b4_distanceThreshold.csv")
B5_DISTANCE_THRESH = os.path.join(BASE_DIR,"distance_threshold","b5_distanceThreshold.csv")
B6_DISTANCE_THRESH = os.path.join(BASE_DIR,"distance_threshold","b6_distanceThreshold.csv")
B7_DISTANCE_THRESH = os.path.join(BASE_DIR,"distance_threshold","b7_distanceThreshold.csv")
B8_DISTANCE_THRESH = os.path.join(BASE_DIR,"distance_threshold","b8_distanceThreshold.csv")
B9_DISTANCE_THRESH = os.path.join(BASE_DIR,"distance_threshold","b9_distanceThreshold.csv")
B10_DISTANCE_THRESH = os.path.join(BASE_DIR,"distance_threshold","b10_distanceThreshold.csv")
#========================================================Events as Key Value pair : Building Specific=========================
B1_EVENT_KEYVALUE = os.path.join(BASE_DIR,"dataset","b1_keyUsrValEncod.pickle")
B2_EVENT_KEYVALUE = os.path.join(BASE_DIR,"dataset","b2_keyUsrValEncod.pickle")
B3_EVENT_KEYVALUE = os.path.join(BASE_DIR,"dataset","b3_keyUsrValEncod.pickle")
B4_EVENT_KEYVALUE = os.path.join(BASE_DIR,"dataset","b4_keyUsrValEncod.pickle")
B5_EVENT_KEYVALUE = os.path.join(BASE_DIR,"dataset","b5_keyUsrValEncod.pickle")
B6_EVENT_KEYVALUE = os.path.join(BASE_DIR,"dataset","b6_keyUsrValEncod.pickle")
B7_EVENT_KEYVALUE = os.path.join(BASE_DIR,"dataset","b7_keyUsrValEncod.pickle")
B8_EVENT_KEYVALUE = os.path.join(BASE_DIR,"dataset","b8_keyUsrValEncod.pickle")
B9_EVENT_KEYVALUE = os.path.join(BASE_DIR,"dataset","b9_keyUsrValEncod.pickle")
B10_EVENT_KEYVALUE = os.path.join(BASE_DIR,"dataset","b10_keyUsrValEncod.pickle")
#========================================================Registered Occupant(Name,Id) : Building Specific=====================
B1_OCCUPANT_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b1_Registered.csv")
B2_OCCUPANT_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b2_Registered.csv")
B3_OCCUPANT_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b3_Registered.csv")
B4_OCCUPANT_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b4_Registered.csv")
B5_OCCUPANT_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b5_Registered.csv")
B6_OCCUPANT_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b6_Registered.csv")
B7_OCCUPANT_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b7_Registered.csv")
B8_OCCUPANT_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b8_Registered.csv")
B9_OCCUPANT_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b9_Registered.csv")
B10_OCCUPANT_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b10_Registered.csv")
#========================================================Visitor Occupants(Name, Id) : Building Specific======================
B1_VISITOR_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b1_Visitor.csv")
B2_VISITOR_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b2_Visitor.csv")
B3_VISITOR_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b3_Visitor.csv")
B4_VISITOR_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b4_Visitor.csv")
B5_VISITOR_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b5_Visitor.csv")
B6_VISITOR_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b6_Visitor.csv")
B7_VISITOR_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b7_Visitor.csv")
B8_VISITOR_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b8_Visitor.csv")
B9_VISITOR_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b9_Visitor.csv")
B10_VISITOR_IDS_INIT = os.path.join(BASE_DIR,"dataset", "b10_Visitor.csv")
#========================================================Zones : Building Specific============================================
B1_ZONES = os.path.join(BASE_DIR,"dataset","b1_zones.csv")
B2_ZONES = os.path.join(BASE_DIR,"dataset","b2_zones.csv")
B3_ZONES = os.path.join(BASE_DIR,"dataset","b3_zones.csv")
B4_ZONES = os.path.join(BASE_DIR,"dataset","b4_zones.csv")
B5_ZONES = os.path.join(BASE_DIR,"dataset","b5_zones.csv")
B6_ZONES = os.path.join(BASE_DIR,"dataset","b6_zones.csv")
B7_ZONES = os.path.join(BASE_DIR,"dataset","b7_zones.csv")
B8_ZONES = os.path.join(BASE_DIR,"dataset","b8_zones.csv")
B9_ZONES = os.path.join(BASE_DIR,"dataset","b9_zones.csv")
B10_ZONES = os.path.join(BASE_DIR,"dataset","b10_zones.csv")
#========================================================Tracks : Building Specific===========================================
#For DSTS
#Building 1
B1_GT_TRACK = os.path.join(BASE_DIR,"groundtruth_tracks","OccupVisitTrack_b1.csv")

#Building 2
B2_GT_TRACK = os.path.join(BASE_DIR,"groundtruth_tracks","OccupVisitTrack_b2.csv")

#Building 3
B3_GT_TRACK = os.path.join(BASE_DIR,"groundtruth_tracks","OccupVisitTrack_b3.csv")

#Building 4
B4_GT_TRACK = os.path.join(BASE_DIR,"groundtruth_tracks","OccupVisitTrack_b4.csv")

#Building 5
B5_GT_TRACK = os.path.join(BASE_DIR,"groundtruth_tracks","OccupVisitTrack_b5.csv")

#Building 6
B6_GT_TRACK = os.path.join(BASE_DIR,"groundtruth_tracks","OccupVisitTrack_b6.csv")

#Building 7
B7_GT_TRACK = os.path.join(BASE_DIR,"groundtruth_tracks","OccupVisitTrack_b7.csv")

#Building 8
B8_GT_TRACK = os.path.join(BASE_DIR,"groundtruth_tracks","OccupVisitTrack_b8.csv")

#Building 9
B9_GT_TRACK = os.path.join(BASE_DIR,"groundtruth_tracks","OccupVisitTrack_b9.csv")

#Building 10
B10_GT_TRACK = os.path.join(BASE_DIR,"groundtruth_tracks","OccupVisitTrack_b10.csv")
#========================================================Estimated State : Building Specific===========================================
#est_state_values_reg
B1_ESTIMATED_STATE_REG = os.path.join(BASE_DIR,"outFiles","b1_state_Estimated_reg.csv")
B2_ESTIMATED_STATE_REG = os.path.join(BASE_DIR,"outFiles","b2_state_Estimated_reg.csv")
B3_ESTIMATED_STATE_REG = os.path.join(BASE_DIR,"outFiles","b3_state_Estimated_reg.csv")
B4_ESTIMATED_STATE_REG = os.path.join(BASE_DIR,"outFiles","b4_state_Estimated_reg.csv")
B5_ESTIMATED_STATE_REG = os.path.join(BASE_DIR,"outFiles","b5_state_Estimated_reg.csv")
B6_ESTIMATED_STATE_REG = os.path.join(BASE_DIR,"outFiles","b6_state_Estimated_reg.csv")
B7_ESTIMATED_STATE_REG = os.path.join(BASE_DIR,"outFiles","b7_state_Estimated_reg.csv")
B8_ESTIMATED_STATE_REG = os.path.join(BASE_DIR,"outFiles","b8_state_Estimated_reg.csv")
B9_ESTIMATED_STATE_REG = os.path.join(BASE_DIR,"outFiles","b9_state_Estimated_reg.csv")
B10_ESTIMATED_STATE_REG = os.path.join(BASE_DIR,"outFiles","b10_state_Estimated_reg.csv")


#========================================================State Relation Estimated: Building Specific===================================
#estimated_SR_reg
B1_EST_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b1_est_SR_full_reg.csv")
B2_EST_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b2_est_SR_full_reg.csv")
B3_EST_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b3_est_SR_full_reg.csv")
B4_EST_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b4_est_SR_full_reg.csv")
B5_EST_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b5_est_SR_full_reg.csv")
B6_EST_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b6_est_SR_full_reg.csv")
B7_EST_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b7_est_SR_full_reg.csv")
B8_EST_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b8_est_SR_full_reg.csv")
B9_EST_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b9_est_SR_full_reg.csv")
B10_EST_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b10_est_SR_full_reg.csv")

#========================================================(Visitor)State Relation Estimated: Building Specific==========================
#est_state_values_visit
B1_ESTIMATED_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b1_state_Estimated_visit.csv")
B2_ESTIMATED_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b2_state_Estimated_visit.csv")
B3_ESTIMATED_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b3_state_Estimated_visit.csv")
B4_ESTIMATED_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b4_state_Estimated_visit.csv")
B5_ESTIMATED_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b5_state_Estimated_visit.csv")
B6_ESTIMATED_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b6_state_Estimated_visit.csv")
B7_ESTIMATED_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b7_state_Estimated_visit.csv")
B8_ESTIMATED_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b8_state_Estimated_visit.csv")
B9_ESTIMATED_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b9_state_Estimated_visit.csv")
B10_ESTIMATED_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b10_state_Estimated_visit.csv")


#========================================================(Visitor)State Relation Estimated: Building Specific===================================
#estimated_SR_visit
B1_EST_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b1_est_SR_full_visit.csv")
B2_EST_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b2_est_SR_full_visit.csv")
B3_EST_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b3_est_SR_full_visit.csv")
B4_EST_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b4_est_SR_full_visit.csv")
B5_EST_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b5_est_SR_full_visit.csv")
B6_EST_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b6_est_SR_full_visit.csv")
B7_EST_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b7_est_SR_full_visit.csv")
B8_EST_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b8_est_SR_full_visit.csv")
B9_EST_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b9_est_SR_full_visit.csv")
B10_EST_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b10_est_SR_full_visit.csv")

#=========================================================(Registered)Estimated valid occupants ===================================================
#estimated_valid_occup
B1_EST_VALID_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","b1_est_valid_occup.csv")
B2_EST_VALID_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","b2_est_valid_occup.csv")
B3_EST_VALID_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","b3_est_valid_occup.csv")
B4_EST_VALID_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","b4_est_valid_occup.csv")
B5_EST_VALID_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","b5_est_valid_occup.csv")
B6_EST_VALID_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","b6_est_valid_occup.csv")
B7_EST_VALID_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","b7_est_valid_occup.csv")
B8_EST_VALID_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","b8_est_valid_occup.csv")
B9_EST_VALID_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","b9_est_valid_occup.csv")
B10_EST_VALID_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","b10_est_valid_occup.csv")
#=========================================================(Registered)Estimated valid tracks ===================================================
#estimated_valid_tracks_reg
B1_EST_VALID_TRACKS_REG = os.path.join(BASE_DIR,"outFiles","b1_est_valid_tracks_reg.csv")
B2_EST_VALID_TRACKS_REG = os.path.join(BASE_DIR,"outFiles","b2_est_valid_tracks_reg.csv")
B3_EST_VALID_TRACKS_REG = os.path.join(BASE_DIR,"outFiles","b3_est_valid_tracks_reg.csv")
B4_EST_VALID_TRACKS_REG = os.path.join(BASE_DIR,"outFiles","b4_est_valid_tracks_reg.csv")
B5_EST_VALID_TRACKS_REG = os.path.join(BASE_DIR,"outFiles","b5_est_valid_tracks_reg.csv")
B6_EST_VALID_TRACKS_REG = os.path.join(BASE_DIR,"outFiles","b6_est_valid_tracks_reg.csv")
B7_EST_VALID_TRACKS_REG = os.path.join(BASE_DIR,"outFiles","b7_est_valid_tracks_reg.csv")
B8_EST_VALID_TRACKS_REG = os.path.join(BASE_DIR,"outFiles","b8_est_valid_tracks_reg.csv")
B9_EST_VALID_TRACKS_REG = os.path.join(BASE_DIR,"outFiles","b9_est_valid_tracks_reg.csv")
B10_EST_VALID_TRACKS_REG = os.path.join(BASE_DIR,"outFiles","b10_est_valid_tracks_reg.csv")

#=========================================================(Visitor)Estimated valid occupants ===================================================
#estimated_valid_visitor
B1_EST_VALID_VISIT = os.path.join(BASE_DIR,"outFiles","b1_est_valid_visit.csv")
B2_EST_VALID_VISIT = os.path.join(BASE_DIR,"outFiles","b2_est_valid_visit.csv")
B3_EST_VALID_VISIT = os.path.join(BASE_DIR,"outFiles","b3_est_valid_visit.csv")
B4_EST_VALID_VISIT = os.path.join(BASE_DIR,"outFiles","b4_est_valid_visit.csv")
B5_EST_VALID_VISIT = os.path.join(BASE_DIR,"outFiles","b5_est_valid_visit.csv")
B6_EST_VALID_VISIT = os.path.join(BASE_DIR,"outFiles","b6_est_valid_visit.csv")
B7_EST_VALID_VISIT = os.path.join(BASE_DIR,"outFiles","b7_est_valid_visit.csv")
B8_EST_VALID_VISIT = os.path.join(BASE_DIR,"outFiles","b8_est_valid_visit.csv")
B9_EST_VALID_VISIT = os.path.join(BASE_DIR,"outFiles","b9_est_valid_visit.csv")
B10_EST_VALID_VISIT = os.path.join(BASE_DIR,"outFiles","b10_est_valid_visit.csv")
#=========================================================(Visitor)Estimated valid tracks ===================================================
#estimated_valid_tracks_visitor
B1_EST_VALID_TRACKS_VISIT = os.path.join(BASE_DIR,"outFiles","b1_est_valid_tracks_visit.csv")
B2_EST_VALID_TRACKS_VISIT = os.path.join(BASE_DIR,"outFiles","b2_est_valid_tracks_visit.csv")
B3_EST_VALID_TRACKS_VISIT = os.path.join(BASE_DIR,"outFiles","b3_est_valid_tracks_visit.csv")
B4_EST_VALID_TRACKS_VISIT = os.path.join(BASE_DIR,"outFiles","b4_est_valid_tracks_visit.csv")
B5_EST_VALID_TRACKS_VISIT = os.path.join(BASE_DIR,"outFiles","b5_est_valid_tracks_visit.csv")
B6_EST_VALID_TRACKS_VISIT = os.path.join(BASE_DIR,"outFiles","b6_est_valid_tracks_visit.csv")
B7_EST_VALID_TRACKS_VISIT = os.path.join(BASE_DIR,"outFiles","b7_est_valid_tracks_visit.csv")
B8_EST_VALID_TRACKS_VISIT = os.path.join(BASE_DIR,"outFiles","b8_est_valid_tracks_visit.csv")
B9_EST_VALID_TRACKS_VISIT = os.path.join(BASE_DIR,"outFiles","b9_est_valid_tracks_visit.csv")
B10_EST_VALID_TRACKS_VISIT = os.path.join(BASE_DIR,"outFiles","b10_est_valid_tracks_visit.csv")

#========================================================(Registered)Reduced State Relation Estimated: Building Specific===========================
#estimated_SR_reduced_reg
B1_EST_STATE_RELATION_REDUCED_REG = os.path.join(BASE_DIR,"outFiles","b1_est_SR_reduced_reg.csv")
B2_EST_STATE_RELATION_REDUCED_REG = os.path.join(BASE_DIR,"outFiles","b2_est_SR_reduced_reg.csv")
B3_EST_STATE_RELATION_REDUCED_REG = os.path.join(BASE_DIR,"outFiles","b3_est_SR_reduced_reg.csv")
B4_EST_STATE_RELATION_REDUCED_REG = os.path.join(BASE_DIR,"outFiles","b4_est_SR_reduced_reg.csv")
B5_EST_STATE_RELATION_REDUCED_REG = os.path.join(BASE_DIR,"outFiles","b5_est_SR_reduced_reg.csv")
B6_EST_STATE_RELATION_REDUCED_REG = os.path.join(BASE_DIR,"outFiles","b6_est_SR_reduced_reg.csv")
B7_EST_STATE_RELATION_REDUCED_REG = os.path.join(BASE_DIR,"outFiles","b7_est_SR_reduced_reg.csv")
B8_EST_STATE_RELATION_REDUCED_REG = os.path.join(BASE_DIR,"outFiles","b8_est_SR_reduced_reg.csv")
B9_EST_STATE_RELATION_REDUCED_REG = os.path.join(BASE_DIR,"outFiles","b9_est_SR_reduced_reg.csv")
B10_EST_STATE_RELATION_REDUCED_REG = os.path.join(BASE_DIR,"outFiles","b10_est_SR_reduced_reg.csv")
#========================================================(Registered)Occupancy Relation Estimated: Building Specific===============================
#estimated_OR_reg
B1_EST_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b1_est_OR_reg.csv")
B2_EST_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b2_est_OR_reg.csv")
B3_EST_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b3_est_OR_reg.csv")
B4_EST_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b4_est_OR_reg.csv")
B5_EST_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b5_est_OR_reg.csv")
B6_EST_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b6_est_OR_reg.csv")
B7_EST_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b7_est_OR_reg.csv")
B8_EST_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b8_est_OR_reg.csv")
B9_EST_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b9_est_OR_reg.csv")
B10_EST_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b10_est_OR_reg.csv")
#
#========================================================(Visitor)Reduced State Relation Estimated: Building Specific===========================
#estimated_SR_reduced_visit
B1_EST_STATE_RELATION_REDUCED_VISIT = os.path.join(BASE_DIR,"outFiles","b1_est_SR_reduced_visit.csv")
B2_EST_STATE_RELATION_REDUCED_VISIT = os.path.join(BASE_DIR,"outFiles","b2_est_SR_reduced_visit.csv")
B3_EST_STATE_RELATION_REDUCED_VISIT = os.path.join(BASE_DIR,"outFiles","b3_est_SR_reduced_visit.csv")
B4_EST_STATE_RELATION_REDUCED_VISIT = os.path.join(BASE_DIR,"outFiles","b4_est_SR_reduced_visit.csv")
B5_EST_STATE_RELATION_REDUCED_VISIT = os.path.join(BASE_DIR,"outFiles","b5_est_SR_reduced_visit.csv")
B6_EST_STATE_RELATION_REDUCED_VISIT = os.path.join(BASE_DIR,"outFiles","b6_est_SR_reduced_visit.csv")
B7_EST_STATE_RELATION_REDUCED_VISIT = os.path.join(BASE_DIR,"outFiles","b7_est_SR_reduced_visit.csv")
B8_EST_STATE_RELATION_REDUCED_VISIT = os.path.join(BASE_DIR,"outFiles","b8_est_SR_reduced_visit.csv")
B9_EST_STATE_RELATION_REDUCED_VISIT = os.path.join(BASE_DIR,"outFiles","b9_est_SR_reduced_visit.csv")
B10_EST_STATE_RELATION_REDUCED_VISIT = os.path.join(BASE_DIR,"outFiles","b10_est_SR_reduced_visit.csv")
#========================================================(Visitor)Occupancy Relation Estimated: Building Specific===============================
#estimated_OR_visit
B1_EST_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b1_est_OR_visit.csv")
B2_EST_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b2_est_OR_visit.csv")
B3_EST_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b3_est_OR_visit.csv")
B4_EST_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b4_est_OR_visit.csv")
B5_EST_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b5_est_OR_visit.csv")
B6_EST_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b6_est_OR_visit.csv")
B7_EST_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b7_est_OR_visit.csv")
B8_EST_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b8_est_OR_visit.csv")
B9_EST_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b9_est_OR_visit.csv")
B10_EST_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b10_est_OR_visit.csv")


#========================================================(Registered)State Values Ground Truth : Building Specific===========================================
#gt_state_values_reg
B1_GT_STATE_REG = os.path.join(BASE_DIR,"outFiles","b1_state_GT_reg.csv")
B2_GT_STATE_REG = os.path.join(BASE_DIR,"outFiles","b2_state_GT_reg.csv")
B3_GT_STATE_REG = os.path.join(BASE_DIR,"outFiles","b3_state_GT_reg.csv")
B4_GT_STATE_REG = os.path.join(BASE_DIR,"outFiles","b4_state_GT_reg.csv")
B5_GT_STATE_REG = os.path.join(BASE_DIR,"outFiles","b5_state_GT_reg.csv")
B6_GT_STATE_REG = os.path.join(BASE_DIR,"outFiles","b6_state_GT_reg.csv")
B7_GT_STATE_REG = os.path.join(BASE_DIR,"outFiles","b7_state_GT_reg.csv")
B8_GT_STATE_REG = os.path.join(BASE_DIR,"outFiles","b8_state_GT_reg.csv")
B9_GT_STATE_REG = os.path.join(BASE_DIR,"outFiles","b9_state_GT_reg.csv")
B10_GT_STATE_REG = os.path.join(BASE_DIR,"outFiles","b10_state_GT_reg.csv")

#========================================================(Registered)State Relation Ground Truth: Building Specific===================================
#gt_sr_full_reg
B1_GT_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b1_gt_SR_full_reg.csv")
B2_GT_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b2_gt_SR_full_reg.csv")
B3_GT_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b3_gt_SR_full_reg.csv")
B4_GT_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b4_gt_SR_full_reg.csv")
B5_GT_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b5_gt_SR_full_reg.csv")
B6_GT_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b6_gt_SR_full_reg.csv")
B7_GT_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b7_gt_SR_full_reg.csv")
B8_GT_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b8_gt_SR_full_reg.csv")
B9_GT_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b9_gt_SR_full_reg.csv")
B10_GT_STATE_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b10_gt_SR_full_reg.csv")
#========================================================(Registered)Occupancy Relation Ground Truth: Building Specific===========================
#gt_or_reg
B1_GT_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b1_gt_OR_reg.csv")
B2_GT_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b2_gt_OR_reg.csv")
B3_GT_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b3_gt_OR_reg.csv")
B4_GT_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b4_gt_OR_reg.csv")
B5_GT_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b5_gt_OR_reg.csv")
B6_GT_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b6_gt_OR_reg.csv")
B7_GT_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b7_gt_OR_reg.csv")
B8_GT_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b8_gt_OR_reg.csv")
B9_GT_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b9_gt_OR_reg.csv")
B10_GT_OCCUPANCY_RELATION_REG = os.path.join(BASE_DIR,"outFiles","b10_gt_OR_reg.csv")
#=======================================================================================


#========================================================(Visitor)State Values Ground Truth : Building Specific===========================================
#gt_state_values_visit
B1_GT_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b1_state_GT_visit.csv")
B2_GT_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b2_state_GT_visit.csv")
B3_GT_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b3_state_GT_visit.csv")
B4_GT_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b4_state_GT_visit.csv")
B5_GT_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b5_state_GT_visit.csv")
B6_GT_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b6_state_GT_visit.csv")
B7_GT_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b7_state_GT_visit.csv")
B8_GT_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b8_state_GT_visit.csv")
B9_GT_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b9_state_GT_visit.csv")
B10_GT_STATE_VISIT = os.path.join(BASE_DIR,"outFiles","b10_state_GT_visit.csv")

#========================================================(Visitor)State Relation Ground Truth: Building Specific===================================
#gt_sr_full_visit
B1_GT_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b1_gt_SR_full_visit.csv")
B2_GT_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b2_gt_SR_full_visit.csv")
B3_GT_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b3_gt_SR_full_visit.csv")
B4_GT_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b4_gt_SR_full_visit.csv")
B5_GT_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b5_gt_SR_full_visit.csv")
B6_GT_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b6_gt_SR_full_visit.csv")
B7_GT_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b7_gt_SR_full_visit.csv")
B8_GT_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b8_gt_SR_full_visit.csv")
B9_GT_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b9_gt_SR_full_visit.csv")
B10_GT_STATE_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b10_gt_SR_full_visit.csv")
#========================================================(Visitor)Occupancy Relation Ground Truth: Building Specific===========================
#gt_or_visit
B1_GT_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b1_gt_OR_visit.csv")
B2_GT_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b2_gt_OR_visit.csv")
B3_GT_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b3_gt_OR_visit.csv")
B4_GT_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b4_gt_OR_visit.csv")
B5_GT_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b5_gt_OR_visit.csv")
B6_GT_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b6_gt_OR_visit.csv")
B7_GT_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b7_gt_OR_visit.csv")
B8_GT_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b8_gt_OR_visit.csv")
B9_GT_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b9_gt_OR_visit.csv")
B10_GT_OCCUPANCY_RELATION_VISIT = os.path.join(BASE_DIR,"outFiles","b10_gt_OR_visit.csv")
#=======================================================================================

#========================================================Database : Building Specific=========================================




#======================================Estimated Values===========================================
#Estimated state Values
ESTIMATED_STATE = os.path.join(BASE_DIR,"outFiles","state_Estimated.csv")
#Estimated Occupant list
#ESTIMATED_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","estimated_occup.csv")
ESTIMATED_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","test_estimated_occup.csv")
#Estimated Valid Tracks
ESTIMATED_VALIDTRACK = os.path.join(BASE_DIR,"outFiles","estimated_validTrack.csv")

#State relation with all occupants
WHOLE_STATE_RELATION_ESTIMATED = os.path.join(BASE_DIR,"outFiles","stateRelation_estimated.csv")
#Reduced State relation
REDUCED_STATE_RELATION_ESTIMATED = os.path.join(BASE_DIR,"outFiles","reduced_SR_estimated.csv")

#State Relation groundtruth
WHOLE_STATE_RELATION_GT = os.path.join(BASE_DIR,"outFiles","stateRelation_GT.csv")
REDUCED_SR_GT = os.path.join(BASE_DIR,"outFiles","reduced_SR_GT.csv")

#==================================================Ground Truth================================================
#Ground truth state Values
GROUNDTRUTH_STATE = os.path.join(BASE_DIR,"outFiles","state_GT.csv")
#State Relation groundtruth
SR_GT_CSTS = os.path.join(BASE_DIR,"outFiles","stateRelation_GT.csv")
#REDUCED_STATE_RELATION_ESTIMATED = os.path.join(BASE_DIR,"outFiles","reduced_SR_estimated.csv")
REDUCED_STATE_RELATION_GT = os.path.join(BASE_DIR,"outFiles","reduced_SR_GT.csv")

GT_OCCUPANTS = os.path.join(BASE_DIR,"outFiles","test_GT_occup.csv")
#Estimated Valid Tracks
GT_VALIDTRACK = os.path.join(BASE_DIR,"outFiles","GT_validTrack.csv")

WHOLE_OR_GT = os.path.join(BASE_DIR,"outFiles","OR_GT_CSTS.csv")

#Occupancy Relation
OCCUPANCY_ESTIMATED = os.path.join(BASE_DIR,"outFiles","or_estimated.csv")
#Database and Query Result Location
