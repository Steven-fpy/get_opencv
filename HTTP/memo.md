## 221201

### HTTP????
    - http란 통신 프로토콜을 일종의 약속으로 규약해 놓은 것
    - 하이퍼텍스트(HTML) 문서를 교환하기 위해 만들어진 Protocal(통신규약)
    - 네트워크를 통해 어떠한 형식으로 통신할지 규정해 놓은 "통신 형식" 혹은
        "통신 구조" (프로토콜)
    - 서버와 클라이언트간의 통신에 사용 

### HTTP 프로토콜의 특징

    - 기본적으로 요청/응답 (Request/Response) 구조
        - 클라이언트가 HTTP Request를 서버에 보내면 서버는 HTTP Response로 응답
        - 모든 통신이 요청과 응답으로 이뤄짐

    - HTTP는 Stateless (무상태)
        - Stateless 란 말드대로 state(상태)를 저장하지 않음
        - 각각의 요청/응답은 독립적인 요청/응답. 이전에 보낸 요청/응답을 저장 하지 않음
        - 여러 요청과 응답의 저장이 필요할때는 쿠키나 세션 등등을 사용

    - HTTP Method 를 통해 통신을 구분
        - GET, POST, PUT, DELETE 등등..(웹페이지는 GET, POST 로 충분)
        - RESTful (REST API) 사용시 Method와 명시한 자원 간에 처리를 일대일 적용가능
            - REST(Representational State Transfer)
            - HTTP Method (POST, GET, PUT, DELETE) <<-->> CRUD(CREATE, READ, UPDATE, DELETE)
### HTTP 프로토콜의 구조 (Request)

    - HTTP Request
        - Start-line
            - 3부분으로 구성 (Ex : GET /path HTTP/1.1)
            - HTTP Method, Request target, HTTP Version
        
        - Header

        - Body
            - 요청의 실제 메시지, 내용
            - 필수로 포함해야 하는 부분은 아님

### HTTP 프로토콜의 구조 (Response)

    - HTTP Response
        -Status-line
            - 응답 상태를 간략히 표시. 3부분으로 구성
            - HTTP Version, Status code, Status text (Ex : HTTP/1.1 200 OK)
        
        - Header
            - 요청과 동일
            - 응답에서만 사용되는 값이 존재 (ex : User-Agent 대신 Server)

        - Body
            - 응답의 실제 메시지, 내용
            - 필수로 포함해야 하는 부분은 아님
            - 주로 HTML, JSON, XML 과 같은 내용이 포함
## 소켓통신

    - 한 번 연결해 놓으면 게속 사용가능