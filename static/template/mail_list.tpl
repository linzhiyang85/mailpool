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
    <main class="mail-container">
        <div class="text-center">
            <h1>免注册邮箱收件</h1>
            <p class="fs-6 text-muted">邮件公开可见, 不定期清理, 请知悉!</p>
            <h2>近期收件</h2>
        </div>
        <div class="mail-list">
            %for mail in mailItems:
                <a href="/addresses/{{mail[0]}}/messages/">
                    <div class="mail-preview" title="点击查看详情" role="alert" aria-live="assertive" aria-atomic="true">
                      <div class="mail-preview-header">
                        <strong class="mail-preview-to">{{mail[0]}}</strong>
                        <small class="mail-preview-received">{{mail[1]['received']}}</small>
                      </div>
                      <div class="mail-preview-subject">
                        {{mail[1]['subject']}}
                      </div>
                    </div>
                </a>
            %end
        </div>

        <div class="view-inbox">
            <h5>直接查看收件箱</h5>
            <div class="input-group mb-3">
              <input id="direct_mail_address" type="text" class="form-control" placeholder="需要查看的收件箱地址" aria-label="Username">
              <span class="input-group-text">@mailpool.xyz</span>
              <button id="go_to_inbox" type="button" class="btn btn-sm btn-light btn-outline-secondary">查看</button>
            </div>
        </div>

        <div class="pick-address">
            <div class="input-group mb-3">
                <h5>随机生成邮箱地址</h5> &nbsp;
                <span id="copy_mail_address_to_clipboard" title="复制到剪切板">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clipboard" viewBox="0 0 16 16">
                        <path d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z"></path>
                        <path d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z"></path>
                    </svg>
                </span>
                <small id="email_copied" class="fade hide" role="alert">邮箱地址已复制!</small>
            </div>
            <div class="input-group mb-3">
              <input id="pick_email_address" type="text" class="form-control" placeholder="请输入任意邮箱地址" aria-label="Username">
              <span class="input-group-text">@mailpool.xyz</span>
              <button id="pick_for_me" type="button" class="btn btn-sm btn-light btn-outline-secondary">帮我选</button>
            </div>
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