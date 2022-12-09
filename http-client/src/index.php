<html>
<head>
    <title>HTML Service</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jost">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <style>
        body {
            font-family: "Jost", sans-serif;
            color: white;
            background-image: url('https://wallpaper.dog/large/445126.jpg');
        }
        .container {
            border: 4px solid white;
            border-radius: 15px;
            background-color: rgb(26, 26, 26);
            margin-top: 15px;
            margin-left: auto;
            margin-right: auto;
        }
        .list-group .list-group-item {
            margin-top: 5px;
            border: 1px solid black;
            border-radius: 15px;
            color: black;
        }
        .form-control.form-control-lg {
            border: 2px solid black;
            border-radius: 15px;
        }
        .btn.btn-info {
            border: 2px solid white;
            border-radius: 15px;
        }
    </style>
</head>
<body>
    <div class="container form">
        <div class="container-fluid">
            <h2>Simple Web Application</h2>
        </div>
        <h2>Find out your text fragments</h2>
        <form action="index.php" method="post">
            <div class="form-group">
                <input id="url" name="url" class="form-control form-control-lg" placeholder="Type URL...">
            </div>
            <button type="submit" class="btn btn-info">Submit</button>
        </form>
    </div>
    <br><br>
    <?php
    if (isset($_POST['url'])) {
        $myCurl = curl_init();
        curl_setopt_array($myCurl, array(
        CURLOPT_URL => 'http://nginxserver/api/?url=' . $_POST['url'],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HEADER => false,
        )
        );
        $response = curl_exec($myCurl);
        curl_close($myCurl);
        $json = json_decode($response);
        $url = $json->url;
        $array = $json->text;
        echo "<div class=\"container response\"><div class=\"container-fluid\"><h2>Найденные фрагменты</h2></div>";
        echo "<ul class=\"list-group\">";
        foreach($array as $value) {
            echo "<li class=\"list-group-item\">" . $value . "</li>";
        }
        echo "</ul></div>";
    }
    ?>
</body>
</html>