def dfscycle (graph, start, visited =None):
    if visited is None: #visited 라는 set 을 생성
        visited = set()
    visited .add(start)
    
    if len(graph[start]&visited) > 1 : #현재 노드와 연결된 노드중에 visited 에 들어있는 노드와
                                   #겹치는 노드가 2개 이상이라면 싸이클이 존재 2번째 방문
                                   #따라서 YES를 print 하고 함수를 종료
        print('YES')
        return None
    
    for next in graph[start]- visited:
        dfscycle (graph, next, visited) #아직 visited안에 없는 인접한 노드를 탐색


  
    
