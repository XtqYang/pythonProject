import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
account_url = "https://<xtq>.blob.core.windows.net"
default_credential = DefaultAzureCredential()
# 创建 BlobServiceClient 对象
blob_service_client = BlobServiceClient(account_url, credential=default_credential)
# 创建一个唯一名称的容器
container_name = str(uuid.uuid4())
# 创建容器
container_client = blob_service_client.create_container(container_name)

# 创建一个本地目录来保存 blob 数据
local_path = "./data"
os.mkdir(local_path)

# 在本地数据目录中创建一个文件以上传和下载
local_file_name = str(uuid.uuid4()) + ".txt"
upload_file_path = os.path.join(local_path, local_file_name)

# 向文件写入文本
file = open(file=upload_file_path, mode='w')
file.write("Hello, World!")
file.close()

# 使用本地文件名作为 blob 的名称创建一个 blob 客户端
blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

print("\n正在上传到 Azure 存储作为 blob:\n\t" + local_file_name)

# 上传创建的文件
with open(file=upload_file_path, mode="rb") as data:
    blob_client.upload_blob(data)
print("\nListing blobs...")

# List the blobs in the container
blob_list = container_client.list_blobs()
for blob in blob_list:
    print("\t" + blob.name)