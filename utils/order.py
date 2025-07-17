def reorder_images(uploaded_files: list, order: list) -> list:
    if not all(0 <= i < len(uploaded_files) for i in order):
        raise ValueError("Invalid Order Index")
    return [uploaded_files[i] for i in order]