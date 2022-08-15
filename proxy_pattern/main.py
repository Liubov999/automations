from proxy_pattern.proxy_txt_reader import TxtProxyReaderWriter
from proxy_pattern.txt_reader import TxtReader
from proxy_pattern.txt_writer import TxtWriter


txt_writer = TxtWriter('users.txt')
proxy_writer = TxtProxyReaderWriter(txt_writer)
txt_reader = TxtReader('users.txt')
proxy_reader = TxtProxyReaderWriter(txt_reader)

print(proxy_reader.read_file())
print('\n')
print(proxy_reader.read_file())