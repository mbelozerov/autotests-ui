from playwright.sync_api import sync_playwright, expect

# Открываем браузер с использованием Playwright
with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
        # Запускаем Chromium браузер в обычном режиме (не headless)
        browser = playwright.chromium.launch(headless=False)
        # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
        context = browser.new_context(storage_state='browser-state.json')
        # Открываем новую страницу в рамках контекста
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_title).to_be_visible()

        block_title_1 = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(block_title_1).to_be_visible()
        expect(block_title_1).to_have_text('There is no results')

        block_title_2 = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(block_title_2).to_be_visible()
        expect(block_title_2).to_have_text('Results from the load test pipeline will be displayed here')

        page.wait_for_timeout(5000)