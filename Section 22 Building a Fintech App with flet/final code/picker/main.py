from flet import *


def main(page: Page):
    page.title = "file picker & Uploads"
    page.bgcolor = colors.WHITE
    page.update()

    page.client_storage.set("colors", ["red", "green", "blue"])

    def container_click(e):
        if page.client_storage.contains_key("flowers"):
            container.visible = True
        else: 
            container.visible = False

        page.update()

    container = Container(
        gradient= LinearGradient(
            colors = page.client_storage.get("colors"),
            begin = alignment.top_left,
            end = alignment.top_right
        ),
        height= 400,
        width = 400,
        on_click= container_click
    )
    def picker_on_result(event: FilePickerResultEvent):
        # print("Explorer")
        upload_button.disabled = False if event.files != None else True
        selected_files.value = ", ".join(list(map(lambda file : file.name, event.files))) if event.files != None else "Explorer Cancelled"
        selected_files.update()

        page.update()

    def upload_files(event):
        uploaded_files = [] 
        
        if file_picker.result != None and file_picker.result.files != None:
            for file in file_picker.result.files:                
                uploaded_files.append(
                        FilePickerUploadFile(
                        file.name,
                        upload_url = page.get_upload_url(f"{file.name}", 60)
                    )
                )
            
            file_picker.upload(uploaded_files)

    file_picker = FilePicker(on_result=picker_on_result)
    selected_files = Text()
    upload_button = ElevatedButton("Upload files",
                            icon=icons.UPLOAD_FILE,
                            disabled = True,
                            on_click = upload_files,
    )

    page.overlay.append(file_picker)
    page.add(
        Column(
            controls = [
                ElevatedButton("Selected files",
                            icon=icons.UPLOAD_FILE,
                            on_click = lambda _ : file_picker.pick_files(
                                allow_multiple=True,
                                allowed_extensions= ["py", "mp4", "mkv"]
                            )
                ),
                selected_files,
                upload_button,
                container
            ]
        )
    )

app(main, view=AppView.FLET_APP_WEB, upload_dir="uploads")
