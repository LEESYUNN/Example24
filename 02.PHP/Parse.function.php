<?php 

    // @link https://stackoverflow.com/questions/21429592/how-to-get-final-redirected-url-after-all-redirection-of-tracking-links/47526664
    function getLastEffectiveUrlByCurl($url) {
        // initialize cURL
        $curl = curl_init($url);
        curl_setopt_array($curl, array(
            CURLOPT_RETURNTRANSFER    => true,
            CURLOPT_FOLLOWLOCATION    => true,
        ));

        // execute the request
        $result = curl_exec($curl);

        // fail if the request was not successful
        if ($result === false) {
            curl_close($curl);
            return null;
        }

        // extract the target url
        $redirectUrl = curl_getinfo($curl, CURLINFO_EFFECTIVE_URL);
        curl_close($curl);

        return $redirectUrl;
    }


    function getContentsBySimpleCurl($url) {
        $curl = curl_init();
        curl_setopt($curl, CURLOPT_URL, $url);
        curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($curl, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/3.0.0.13');
        curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($curl, CURLOPT_HEADER, 0); 
        $data = curl_exec($curl);
        curl_close($curl);
        return $data;
    }


    // @link https://www.cnblogs.com/oxspirt/p/5979709.html
    function getContentsByDetailCurl($URI, $isHearder=false, $post=false) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $URI);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_TIMEOUT, 60);          //单位 秒，也可以使用
        // curl_setopt($ch, CURLOPT_NOSIGNAL, 1);     //注意，毫秒超时一定要设置这个
        // curl_setopt($ch, CURLOPT_TIMEOUT_MS, 200); //超时毫秒，cURL 7.16.2中被加入。从PHP 5.2.3起可使用
        curl_setopt($ch, CURLOPT_HEADER, $isHearder);
        curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36');
        // curl_setopt($ch, CURLOPT_COOKIEFILE, dirname(__FILE__)."/tmp.cookie");
        // curl_setopt($ch, CURLOPT_COOKIEJAR, dirname(__FILE__)."/tmp.cookie");

        if(strpos($URI, 'https') === 0){

            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
            curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
        }
        if($post){
            curl_setopt ($ch, CURLOPT_POST, 1);
            curl_setopt ($ch, CURLOPT_POSTFIELDS, $post);
        }
        $result = curl_exec($ch);
        curl_close($ch);
        return $result;
    }





