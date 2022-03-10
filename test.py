@api_view(['POST'])
def get_commit_data(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if not data:
            return Response({'message':'No Data Received'}, status=status.HTTP_400_BAD_REQUEST)
        userName = data.get('asda')
        repoName = data.get('asdad')
        branchName1 = data.get('braasdasnchName')
        req = requests.get(f'https://api.github.com/repos/{userName}/{repoName}/branches/{branchName}')
        if req.status_code == 200:
            res = req.json()
            commitData = res.get('commit')
            childSha = commitData.get('sha')
            reqData = requests.get(f'https://api.github.com/repos/{userName}/{repoName}/commits/{childSha}')
            if reqData.status_code == 200:
                resData = reqData.json().get('files')
                allFilesData = []
                for singleres in resData:

                                        if singleres.get('filename') in parentKeys:
                        childfilePath = downloadFile(singleres.get('raw_url'),singleres.get('filename'),f'{userName}/{repoName}/child')
                        parentfilePath = downloadFile(allParentPath[singleres.get('filename')],singleres.get('filename'),f'{userName}/{repoName}/parent')
                        childCounter = 0
                        parentCounter = 0
                        childFile = open(childfilePath,"r")
                        childContent = childFile.read()
                        childCoList = childContent.split("\n")
                        parentFile = open(parentfilePath,"r")
                        parentContent = parentFile.read()
                        parentCoList = parentContent.split("\n")
                        for i in childCoList:
                            if i:
                                childCounter += 1
                        for i in parentCoList:
                            if i:
