import admin_privilage as admin # type: ignore

joe_block = admin.Administrator("joe", "block", 31)
joe_block.privilages.show_privilages(["can undo post", "can edit post"])