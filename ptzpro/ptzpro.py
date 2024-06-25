import hid


class PTZPro:
    def __init__(self, vendor_id=1133, product_id=2143):
        self.device = hid.device()
        self.device.open(vendor_id, product_id)

    def send_command(self, report_id, value):
        command = [0x00] * 32
        command[0] = report_id & 0xff
        command[1] = value
        self.device.write(command)

    def pan_right(self):
        self.send_command(0x0b, 0x02)  # Report ID for FarEndPTZType, Command value for Pan Right

    def pan_left(self):
        self.send_command(0x0b, 0x03)  # Report ID for FarEndPTZType, Command value for Pan Left

    def tilt_up(self):
        self.send_command(0x0b, 0x00)  # Command value for Tilt Up

    def tilt_down(self):
        self.send_command(0x0b, 0x01)  # Command value for Tilt Down

    def zoom_in(self):
        self.send_command(0x0b, 0x04)  # Command value for Zoom In

    def zoom_out(self):
        self.send_command(0x0b, 0x05)  # Command value for Zoom Out

    def mic_mute(self):
        self.send_command(0x09, 0x01)  # Example command value for Mic Mute

    def mic_unmute(self):
        self.send_command(0x09, 0x00)  # Example command value for Mic Unmute

    def close(self):
        self.device.close()