from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Create a mock PHP server response for empty state
    # Since we can't easily spin up the full PHP server with DB connection in this environment without credentials,
    # we will rely on the static file verification or the test script output.
    # However, to visualize the HTML structure we modified, we can load the HTML content directly
    # or use a simple python http server to serve a static HTML if we dump it.

    # Alternative: run the php verification script and capture its output to a file, then load that file.
    # We already have tests/verify_empty_state.php which outputs text.
    # Let's try to run a modified version of verify_empty_state.php that outputs the HTML to a file.

    import subprocess

    # Generate the HTML with empty state using PHP
    php_code = """
<?php
define('APP_NAME', 'TestApp');
function h($s){ return htmlspecialchars($s ?? '', ENT_QUOTES, 'UTF-8'); }
$indexContent = file_get_contents(__DIR__ . '/public/index.php');
$indexContent = str_replace("require_once __DIR__ . '/../app/db.php';", "", $indexContent);
$pattern = '/\$q = trim\(\$_GET\[\\'q\\'\] \?\? \\'\\'\\);.*\$movies=\$st->fetchAll\(\);/s';
$replacement = '$q = "test query"; $movies = [];';
$indexContent = preg_replace($pattern, $replacement, $indexContent);
// Fix relative path for css since we will save this in root or public
$indexContent = str_replace('href="/assets/style.css"', 'href="public/assets/style.css"', $indexContent);
eval('?>' . $indexContent);
?>
"""
    with open('generate_preview.php', 'w') as f:
        f.write(php_code)

    subprocess.run(['php', 'generate_preview.php'], stdout=open('preview.html', 'w'))

    # Now load the generated HTML
    import os
    file_path = os.path.abspath('preview.html')
    page.goto(f'file://{file_path}')

    # Take screenshot
    page.screenshot(path='.Jules/verification/empty_state.png')

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
