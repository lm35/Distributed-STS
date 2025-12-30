# Distributed-STS
Distrbuted State Transition System Approach
A Python-based simulation framework was implemented to emulate occupant tracking in a multi-building indoor smart environment. Although no graphical simulation interface was created, the environment captures realistic occupant behaviors and inter-zone transitions through event-driven logic. The simulation replicates the processes of detecting, recognizing, and tracking individuals by creating synthetic event sequences. It also facilitates seamless and systematic state updates while ensuring consistent management of state transitions across all buildings. This approach enabled systematic assessment of the scalability and performance of both centralized and distributed tracking models within a controlled and reproducible environment.

Face recognition was employed as the primary biometric modality throughout the experiments, with a ResNet-34 deep learning model. The output from the recognizer is transformed into event probabilities. These probabilities were organized into a time-sequenced pool aligned with the generated event sets or occupant trajectories. Each element within an event set is represented as an ordered tuple comprising the event ID, timestamp of occurrence, zone of occurrence, and the ground-truth occupant ID.A sample element from an event set is similar is as follows. $$e1281, 2025-03-26 \: 15\colon22\colon17, mailroom_{3},o_{10}^{10}$$

 The data model is applied to both actual and estimated state probabilities, which are maintained as separate state databases to facilitate efficient retrieval during query-based comparisons. 

The building is divided into $9$ zones, namely entrance, mail room, office, lounge, conference room, classroom, cafeteria, exit and transition zone. A simulation run represents a complete sequence of recognition events that would typically occur over a day for a subset of individuals available within various buildings. The trajectory of a person might include intra-building and inter-building movements. Any intra-building movement of an occupant (trajectory) includes an entry event into the building, intermediate movements across multiple zones within that building, followed by an exit to the transition zone through the exit zone. Movement of an individual from one building to another constitutes inter-building movements. If the trajectory of an occupant includes zones from multiple buildings, then the occupant exhibits inter-building movements. We define valid paths for any building b_u based on a grammar that adheres to layout and zone adjacencies. 
$script\_start \rightarrow entrance$ \\
$ script\_end \rightarrow exit, transit$ \\
$ teach \rightarrow mailroom, entrance, classroom$ \\
$ teach \rightarrow lounge, entrance, classroom $ \\
$ goto\_office \rightarrow mailroom, lounge, office $ \\
$ goto\_office \rightarrow lounge, mailroom, office$ \\
$ lunch\_break \rightarrow lounge, entrance, cafeteria$ \\
$ lunch\_break \rightarrow mailroom, entrance, cafeteria$ \\
$meeting \rightarrow lounge, office, conference \: room$\\
$meeting \rightarrow lounge, mailroom, conference \: room $
# Face Data Collection for Proprietary Dataset}

As part of our experimental evaluation, we utilized a publicly available dataset. Our dataset comprises face images of 100 individuals, with 40 images collected per individual. For each person, the images were randomly partitioned into a reference set and a test set using a 3:1 ratio.
# Face Detection and Recognition

The input to the state transition system model is derived from a face recognizer. We perform face detection and recognition with OpenCV, Python 3.8 and deep learning. We employ the Dlib library created by Davis King for face detection and face embedding generation. Further, the face_recognition, a Python wrapper for the Dlib library, is used for generating the distance score between reference images and test images. The face_locations function within face_recognition library returns a list of tuples, each representing the coordinates of a bounding box around the detected faces. 

The face_encodings module generates a 128-dimensional encoding for each face. This module uses the implementation of ResNet-34 architecture from Dlib. This implementation of ResNet-34 architecture in Dlib itself uses fewer layers and half the number of filters. Further, we use a face_distance function to get the Euclidean distance between the test image and the images in the reference database. The face detection module in Dlib uses Histogram Oriented Gradients (HOG) with Support Vector Machine (SVM) as well as CNN-based detectors. The module is capable of detecting frontal face images, returning a list of bounding boxes indicating the location of a detected face. The HOG with SVM detector is good for faster detection, but it is not suitable for images with extreme pose variation. However, the CNN-based approach is suitable for frontal and non-frontal faces, but is slower in action. The generated distance scores are further converted to occupant probability pairs as discussed for CSTS approach and for DSTS approach.
# Database Design

The CSTS Database is designed to handle and preserve vital data from the wide-area in terms of state relations and occupancy relations. Its structure is organized into a database file named csts_moit.sqlite3, which comprises two main tables: the state relation table and the occupancy relation table. Below is an overview of their structure and the details of their respective columns. The information in the state relation table is generated in reference to the state relation data model between occupants and zones, at various instances of time(time at which events occur), and varying state probability values. The state probability values correspond to the occupants' corresponding state information. 
The schema of the state relation table for CSTS is defined as follows:

    OccupantID (TEXT): Unique identifier for each occupant.
   ZoneID (TEXT): Unique identifier for a zone.
    Probability (REAL): Likelihood of the occupant being in a given zone.
    Time(TEXT): Timestamp corresponding to the recorded event.


The occupancy relation table information is generated in reference to the occupancy-relation data model. It provides a time range during which an occupant is associated with a specific zone. The schema of the occupancy relation table for CSTS is defined as follows
    OccupantID (TEXT): Unique identifier for each occupant.
    ZoneID (TEXT): Unique identifier for a zone.
    Probability (REAL): Likelihood of the occupant's presence in a given zone.
    FromTime (TEXT): Starting time for the occupancy relation.
    ToTime (TEXT): Ending time for the occupancy relation.

Similar to the CSTS approach, the DSTS approach employs databases to manage the state information of the smart space. This is done with a focus on efficiently handling the large volume and the multimedia nature of the data. However, while CSTS employs a single database and two tables corresponding to each data model for the wide-area, the DSTS approach extends the distributed strategy in database design as well. The DSTS approach maintains separate databases for each building within the wide-area. Even though the DSTS approach employs a distribution approach, both methods are based on a common data model that includes state-relation and occupancy-relation. These models serve as the foundation for the database design. 

The distributed approach is realized with horizontal partitioning applied to the CSTS database. We introduce building-specific partitioning in the database design, where each building maintains its implementation of the state-relation and occupancy-relation data models. This enables efficient building-level data management. Horizontal partitioning, unique to the DSTS approach, accounts for two occupant classes: the registered occupant class and the visitor class. To support this, the database for each building contains four distinct tables: state relation and occupancy relation tables for registered occupants, and separate state relation and occupancy relation tables for visitors. The visitor data for each building is managed through a static visitor table that accounts for the potential visitor set. This partitioning strategy ensures scalability and efficient handling of building-specific and occupant-specific data.

The schema of the state relation table for registered occupants for a particular building of DSTS is defined as follows:

    OccupantID (TEXT): Unique occupant identifier for each registered occupant of building b_u.
    ZoneID (TEXT): Unique zone identifier for building b_u.
    Probability (REAL): Likelihood of the occupant being in a given zone.
    Time (TEXT): Timestamp corresponding to the recorded event.


The occupancy relation table information is generated in reference to the occupancy-relation data model. It provides a time range during which an occupant is associated with a specific zone. The schema of the occupancy relation table for registered occupants of a building b_u in DSTS is defined as follows:

  OccupantID (TEXT): Unique occupant identifier for each visitor of the building b_u.
ZoneID (TEXT): Unique zone identifier for building b_u.
   Probability (REAL): Likelihood of the visitor's presence in a given zone.
    FromTime (TEXT): Starting time for the occupancy relation.
 ToTime (TEXT): Ending time for the occupancy relation.


In the DSTS approach, the state relation and occupancy relation tables for visitors are constructed based on the potential visitor set, where each occupant ID corresponds to the associated visitor set for building b_u in a similar manner as defined for registered occupants in DSTS.
