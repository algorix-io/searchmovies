<?php
// Mocks for index.php environment
define('APP_NAME', 'TestApp');
function h($s){ return htmlspecialchars($s ?? '', ENT_QUOTES, 'UTF-8'); }

// Read the index.php file
$indexContent = file_get_contents(__DIR__ . '/../public/index.php');

// Remove the DB requirement
$indexContent = str_replace("require_once __DIR__ . '/../app/db.php';", "", $indexContent);

// Remove the DB query logic block
// We'll replace the whole block from $q = ... to the end of $movies = ...
// This is fragile but necessary without dependency injection
$pattern = '/\$q = trim\(\$_GET\[\'q\'\] \?\? \'\'\);.*\$movies=\$st->fetchAll\(\);/s';
$replacement = '$q = "test query"; $movies = [];'; // Simulate empty result
$indexContent = preg_replace($pattern, $replacement, $indexContent);

// Save as a temporary file
$tempFile = __DIR__ . '/../public/temp_index_test.php';
file_put_contents($tempFile, $indexContent);

// Capture output
ob_start();
include $tempFile;
$output = ob_get_clean();

// Clean up
unlink($tempFile);

// Assertions
$failed = false;

if (strpos($output, 'No movies found') === false) {
    echo "FAIL: 'No movies found' message missing.\n";
    $failed = true;
} else {
    echo "PASS: 'No movies found' message present.\n";
}

if (strpos($output, 'aria-label="Search movies"') === false) {
    echo "FAIL: Search input missing aria-label.\n";
    $failed = true;
} else {
    echo "PASS: Search input has aria-label.\n";
}

if ($failed) {
    exit(1);
}

echo "All checks passed!\n";
