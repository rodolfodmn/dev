<?php
shell_exec('magento-cloud db:dump');
$createDB = "CREATE DATABASE mage_veiling";
$updateUrlToLocal = "UPDATE core_config_data SET value='http://veiling-holambra.local/' WHERE value like '%mcstaging.veilingonline.com.br%'";
