<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
<!--    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">-->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/static/css/custom.css" rel="stylesheet">

    <title>喵铺 - 临时邮箱助手</title>
</head>
<body>
    <main class="message-container">
        <div class="text-center">
            <h1>{{inboxName}} 的收件箱</h1>
            <p class="fs-6 text-muted">邮件公开可见, 不定期清理, 请知悉!</p>
        </div>
        <button id="message-toggle" data-status="#">Toggle</button>
        <div class="accordion" id="message-list">
            %for message in messageItems:
              <div class="accordion-item">
                <h2 class="accordion-header">
                  <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{{message['id']}}" aria-expanded="true" aria-controls="collapseOne">
                    发件人: {{message['from']}} | 接收时间: {{message['received']}}
                    <br>
                    标题: {{message['subject']}}
                  </button>
                </h2>
                <div id="collapse{{message['id']}}" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#message-list">
                  <div class="accordion-body">
                    {{message['body']}}
                  </div>
                </div>
              </div>
            %end
        </div>
    </main>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="/static/js/bootstrap.bundle.min.js"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-W8fXfP3gkOKtndU4JGtKDvXbO53Wy8SZCQHczT5FMiiqmQfUpWbYdTil/SxwZgAN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.min.js" integrity="sha384-skAcpIdS7UcVUC05LJ9Dxay8AXcDYfBJqt1CJ85S/CFujBsIzCIv+l9liuYLaMQ/" crossorigin="anonymous"></script>
    -->
    <script src = "/static/js/faker.min.js" type = "text/javascript"></script>
    <script src = "/static/js/custom.js" type = "text/javascript"></script>
</body>
</html>