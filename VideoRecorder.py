import threading
import random
import picamera

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
        #self.camera.awb_mode = 'off'
        #self.camera.awb_mode = 'sunlight'
        #self.camera.awb_mode = 'fluorescent'
        #self.camera.awb_mode = 'incandescent'

    def record(self):
        self.camera.start_preview(alpha = 200)
        self.camera.start_recording(self.file_name)

    def stop(self):
        self.camera.stop_recording()
        self.camera.stop_preview()

    def start(self, file_name, file_dir):
        self.file_name = '{}/{}.h264'.format(file_dir, file_name)

        video_thread = threading.Thread(target=self.record)
        video_thread.start()
