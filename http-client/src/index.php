<html>
<head>
    <title>HTML Service</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
    <h2>App Page</h2>
    <h3>HTML Text Selector</h3>
    <form action="index.php" method="post">
        <input id="url" name="url" class="form-control" placeholder="Type URL...">
        <input type="submit" class="btn btn-success" value="Execute">
    </form>
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
        echo "<h3>URL: " . $url . "</h3>";
        echo "<ul>";
        foreach($array as $value) {
            echo "<li>" . $value . "</li>";
        }
        echo "</ul>";
    }
    ?>
</body>
</html>