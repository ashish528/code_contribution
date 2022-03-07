@api_view(['POST'])
def get_commit_data(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if not data:
            return Response({'message':'No Data Received'}, status=status.HTTP_400_BAD_REQUEST)
        userName = data.get('asda')
        repoName = data.get('sd')
        branchName = data.get('braasdasnchName')
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
