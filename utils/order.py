def reorder_images(uploaded_files: list, order: list) -> list:
    return [uploaded_files[i] for i in order]