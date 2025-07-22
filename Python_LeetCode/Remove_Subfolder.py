class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        for f in folder:
            is_subfolder = False
            for parent in result:
                if f.startswith(parent + "/"):
                    is_subfolder = True
                    break
            if not is_subfolder:
                result.append(f) 
        return result
