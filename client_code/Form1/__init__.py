from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_click(self, **event_args):
    # Lấy giá trị từ các TextBox
    network_address = self.text_box_network.text
    num_subnets = int(self.text_box_subnets.text)

    # Gọi hàm subnet_division từ Server Module
    subnets = anvil.server.call('subnet_division', network_address, num_subnets)

    # Hiển thị kết quả lên Label
    self.label_result.text = '\n'.join(subnets)


