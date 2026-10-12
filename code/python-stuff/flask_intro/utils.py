def create_file(data: bytes, file_path: str):
    with open(file_path, "wb") as f:
        f.write(data)