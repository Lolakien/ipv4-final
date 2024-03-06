import anvil.server
import ipaddress

@anvil.server.callable
def subnet_division(network_address, num_subnets):
    # Chuyển đổi địa chỉ mạng vào kiểu ipaddress.IPv4Network
    network = ipaddress.IPv4Network(network_address)

    # Tính số lượng IP trong mỗi mạng con
    subnet_prefix = network.prefixlen + int(network.max_prefixlen / num_subnets)

    # Tạo danh sách các mạng con
    subnets = list(network.subnets(new_prefix=subnet_prefix))

    # Trả về danh sách các mạng con đã chia
    return [str(subnet) for subnet in subnets]