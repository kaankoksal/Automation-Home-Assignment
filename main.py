from runSpider import runSpider
from top5 import Top5
from uploadToDrive import Upload

# Initiate the scraping
runSpider()

# Get the Top 5 most frequent cast members
cast_members = Top5()
cast_members.get_top5()

# Upload csv to Drive as Google Spreadhseet
drive_upload = Upload()
drive_upload.driveUpload()