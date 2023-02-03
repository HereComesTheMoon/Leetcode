class Solution:
    def simplifyPath(self, path: str) -> str:
        steps = path.split('/')
        res = []
        for step in steps:
            if not step:
                continue
            if step == '.':
                continue
            if step == '..':
                if res:
                    res.pop()
                continue
            res.append(step)
        return '/' + '/'.join(res)


        