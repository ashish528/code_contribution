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
                                
                                
                                                            lineadded.append(singleline[1:])
                    send_data = []
                    if (linedeleted and lineadded):
                        if len(linedeleted) > len(lineadded):
                            count = len(linedeleted) - len(lineadded)
                            for i in range(len(lineadded)):
                                send_data.append({'line_deleted':linedeleted[i],'line_added':lineadded[i],'lineLanguage':guess.language_name(lineadded[i])})
                            for i in linedeleted[-count:]:
                                send_data.append({'line_deleted':i})
                        elif len(lineadded) > len(linedeleted):
                            count = len(lineadded) - len(linedeleted)
                            for i in range(len(linedeleted)):
                                send_data.append({'line_deleted':linedeleted[i],'line_added':lineadded[i],'lineLanguage':guess.language_name(lineadded[i])})
                            for i in lineadded[-count:]:
                                send_data.append({'line_added':i})
                        else:
                            for i in range(len(lineadded)):
                                send_data.append({'line_deleted':linedeleted[i],'line_added':lineadded[i],'lineLanguage':guess.language_name(lineadded[i])})
                    else:
                        if linedeleted:
                            for i in linedeleted:
                                send_data.append({'line_deleted':i,'lineLanguage':guess.language_name(i)})
                        elif lineadded:
                            for i in lineadded:
                                send_data.append({'line_added':i,'lineLanguage':guess.language_name(i)})
                    fileExtData = '\n'.join(lineadded)
                    codeLang = guess.language_name(fileExtData)
