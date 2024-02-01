-----Storage Class and Data Management-----
Selected Storage Class: [actual storage class]Standard/Intelligent-Tiering/Standard-IA (Infrequent Access)/One Zone-IA/Glacier/Glacier Deep Archive/Outposts
Workload Characteristics: [actual workload characteristics]True/False

-----Security and Compliance-----
Encryption at Rest: [actual value]True/False
Encryption in Transit: [actual value]True/False
Industry Standards Compliance: [actual value]True/False

-----Scalability Requirements-----
Number of Users: [actual value]
Data Growth Rate: [actual data growth rate]high/medium/low

Analyzing Storage Classes and Performing Actions:
Object: example_object_key_1, Storage Class: STANDARD, Cost: $[actual cost]
Object: example_object_key_2, Storage Class: INTELLIGENT_TIERING, Cost: $[actual cost]
...

Generating S3 Bucket Report:
Report for S3 Bucket: [your_bucket_name] ## if availble it provide output
========================================
Storage Classes:
  - STANDARD: 00 objects
  - INTELLIGENT_TIERING: 00 objects
  - GLACIER: 00 objects
  - ONEZONE_IA: 00 objects

Bucket Structure:
  - Total Objects: 000
  - Folders: 00
  - Nested Folders: 00

Lifecycle Management:
  - Transitioning to GLACIER after 30 days for specific objects
  - No expiration rules
...
Report generation complete.
