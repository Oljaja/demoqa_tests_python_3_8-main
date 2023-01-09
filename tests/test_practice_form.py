from selene.support.shared import browser

from demoqa_tests.model.pages import practice_form


def test_fill_practice_form(window_size):
    browser.open('https://demoqa.com/automation-practice-form')
    practice_form.set_first_name('Ona')
    practice_form.set_last_name('Nov')
    practice_form.set_email('test@gmail.com')
    practice_form.select_gender('Other')
    practice_form.set_mobile_number('8999955555')
    practice_form.set_birthday(day=3, month=1, year='2023')
    practice_form.set_subjects('Economics')
    practice_form.select_hobbies('Sports')
    practice_form.select_picture('111.jpg')
    practice_form.set_current_address('Angelovo')
    practice_form.select_state('Haryana')
    #practice_form.select_city('Panipat')
    practice_form.submit()


    practice_form.check_results('Ona Nov', 'test@gmail.com', 'Other', '8999955555',
                                '03, 01,2023', 'Economics', 'Sports', '111.png',
                                'Angelovo', 'Haryana Panipat')
