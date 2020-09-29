import threading
import random
import picamera
from fractions import Fraction

class VideoRecorder:
    def __init__(self):
        self.file_name = 'default_name' # This should be replaces with a value given in self.start()
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1280, 720)
        self.camera.framerate = 25
        self.camera.rotation = 180
        #self.camera.awb_mode = 'cloudy'
        #self.camera.awb_mode = 'shade'
        #self.camera.awb_mode = 'auto'
        #self.camera.awb_mode = 'tungsten'
        #self.camera.awb_mode = 'flash'
        #self.camera.awb_mode = 'horizon'
        self.camera.awb_mode = 'off'
        #self.camera.awb_mode = 'sunlight'
        #self.camera.awb_mode = 'fluorescent'
        #self.camera.awb_mode = 'incandescent'
        #self.camera.awb_gains = (Fraction(395, 256), Fraction(245, 128))
        #self.camera.awb_gains = (Fraction(395, 256), Fraction(395, 256)) # Good
        #self.camera.awb_gains = (Fraction(200, 256), Fraction(200, 256)) # Green
        #self.camera.awb_gains = (Fraction(300, 256), Fraction(300, 256)) # Gult?
        self.camera.awb_gains = (Fraction(350, 256), Fraction(350, 256)) # Green
        print('I' + str(self.camera.awb_gains))

    def record(self):
        self.camera.start_preview(alpha = 200)
        self.camera.start_recording(self.file_name)
        print('R' + str(self.camera.awb_gains))

    def stop(self):
        print('E' + str(self.camera.awb_gains))
        self.camera.stop_recording()
        self.camera.stop_preview()

    def start(self, file_name, file_dir):
        self.file_name = '{}/{}.h264'.format(file_dir, file_name)

        video_thread = threading.Thread(target=self.record)
        video_thread.start()
        print('B' + str(self.camera.awb_gains))
