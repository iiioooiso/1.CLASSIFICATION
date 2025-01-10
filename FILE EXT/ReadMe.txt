BT23CSD010

Data Classification :
1.Structured 
   Tabular data like SQL databases, CSV , Excel or JSON.
   Typically easier to store, query, and analyze.
 Ex : Customer data, sales records.

2.Unstructured 
   Don't have a predefined structure
Ex : Social media posts, medical images, audio files, video files, emails.


Types of data formats :
Images: JPEG, PNG, GIF, BMP.
Libraries: OpenCV, PIL (Pillow), scikit-image.

Audio:
Common formats: WAV, MP3, FLAC.
Libraries: Pydub, librosa, wave.

Text:
Common formats: ASCII, JSON, XML, CSV.
Libraries: pandas (for CSV), json (for JSON), regex (for text parsing).

Video:
Common formats: MP4, AVI, MKV.
Libraries: OpenCV, moviepy.


CLASSIFICATION : 

1. Basic CLassification by File Extention
   Pillow (PIL) for image processing.
   Pydub for audio processing (it uses mediainfo to check audio file info).
   OpenCV for video processing.
   Python standard json for handling JSON files and basic text files.
   NOTE : Make sure file is released ( not locked ) 
2. Using File Metadata: Multipurpose Internet Mail Extension ( MIME )
   Library : python-magic

3. AI/ML :
   If File Extention are misleading or in case of mixed data!
   TensorFlow or PyTorch

4. Integration with Cloud-Based File Org. : 
   AWS S3, Google Cloud Storage, or Azure Blob Storage


Existing Tech : 
FileBot
Apache Tike
AWS S3, Google Cloud Storage



Our Solution's benefit : 
Customization
Cost
Control 


