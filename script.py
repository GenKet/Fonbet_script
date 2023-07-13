from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time, random
from datetime import datetime, date

# Инициализация веб-драйвера (например, для Chrome)
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")

driver_path = "C:\Fonbet\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
# Открытие веб-страницы
driver.get("https://www.fonbet.by")

key= random.randint(500000,1000000)
new_content = str(key)

while(True):
    element = ""
    class_name1 = ""
    name_of_events = []
    koefs = []
    stavki = []
    football = """<span class="sport-icon--3dTpaN _use_color_settings--2h94AH" style="background-image: url(&quot;//origin.by0e87-resources.by/ContentCommon/Logotypes/SportKinds/new-design/white_new/1-football.svg&quot;);"></span>"""
    basketball = """<span class="sport-icon--3dTpaN _use_color_settings--2h94AH" style="background-image: url(&quot;//origin.by0e87-resources.by/ContentCommon/Logotypes/SportKinds/new-design/white_new/3-basketball.svg&quot;);"></span>"""
    tennis = """<span class="sport-icon--3dTpaN _use_color_settings--2h94AH" style="background-image: url(&quot;//origin.by0e87-resources.by/ContentCommon/Logotypes/SportKinds/new-design/white_new/table-tennis.svg&quot;);"></span>"""
    hockey = """<span class="sport-icon--3dTpaN _use_color_settings--2h94AH" style="background-image: url(&quot;//origin.by0e87-resources.by/ContentCommon/Logotypes/SportKinds/new-design/white_new/2-hockey.svg&quot;);"></span>"""

    
    while(element == ""):
        try:
            wait = WebDriverWait(driver, 3)

            class_name = 'header__login-balance'

            # Заменить содержимое блока
            element = driver.find_element('css selector', f'.{class_name}')
            driver.execute_script("arguments[0].innerText = arguments[1]", element, new_content)

            class_name99 = 'tab2--6tYBSA'
            # Заменить содержимое блока
            new_content99 = "История"
            element99 = driver.find_element('css selector', f'.{class_name99}')
            driver.execute_script("arguments[0].innerText = arguments[1]", element99, new_content99)
        except:
            print("Нет значения")
        finally:
            while (class_name1 == ""):
                try:
                    class_name = "header__login-balance"
                    class_name1 = "modal-container"
                    # modal = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-container")))
                    # script = f"var element = document.getElementsByClassName('{class_name1}')[0]; element.parentNode.removeChild(element);"
                    # driver.execute_script(script)

                    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button--9z8aUQ')))

                    def stop_event_propagation(driver, element):
                        driver.execute_script("arguments[0].addEventListener('click', function(event) { event.stopPropagation(); });", element)

                    time.sleep(7)
                    stop_event_propagation(driver, button)

                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")

                    now1 = date.today()
                    current_data = "{}.{}".format(now1.day, now1.month)

                    express_coupons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "stake-wide--3LnKdO")))
                    count = len(express_coupons)

                    if (count == 1):

                        element_with_class1 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "event-data--1UykiN")))
                        name_of_event = element_with_class1.text

                        element_with_class2 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "v-current--6su1Qn")))
                        koef = element_with_class2.text

                        element_with_class3 = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"column3--1r5hIk")))
                        stavka = element_with_class3[1].text

                        input_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sum-panel__input--5a9SqV")))
                        value = input_element.get_attribute("value")
                        value2 = value

                        valuekoef = float(value2) * float(koef)
                        value_koef = round(valuekoef,2)
                        sell = float(value2)*0.92
                        Sell = round(sell,2)


                        class_name2 = "new-coupon--5cY6lQ"
                        modal1 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new-coupon--5cY6lQ")))
                        script1 = f"var element = document.getElementsByClassName('{class_name2}')[0]; element.parentNode.removeChild(element);"
                        driver.execute_script(script1)

                        script2 = f"""
                        var div = document.createElement("div");
                        div.innerHTML = `
                            <div class="new-coupon--5cY6lQ" style="background-color: rgb(37, 62, 91);"><div class="empty--4pI7r2" style="background-color: rgb(37, 62, 91);"><span class="caption-area--6Yqezu">Выберите исход события, чтобы заключить пари</span><div class="switch-area--IywgSo"><span class="switch--1HvPTt _use_color_settings--2h94AH _off--4i6Yy3"></span><span class="text--2D5yKe"><span style="cursor: pointer;">Пари в один клик</span></span></div><div style="height: 16px;"></div></div><div class="separator--5ixw9J" style="height: 1px; background-color: rgb(37, 62, 91);"></div></div>
                            <div class="coupon-list--UluSeE _top-padding--6VyvQR" style="background-color: rgb(37, 62, 91);"><article class="coupon--61Qt1m"><div class="coupon__head--5nsL30"><div class="coupon__iconGeometry--4HFE4v svgDelete--4w0Fgk flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 15 15" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M3.46143 11.3242L11.4614 3.32422M3.46143 3.32422L11.4614 11.3242L3.46143 3.32422Z" stroke="currentColor"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M2.4 1.5c-.5 0-.9.4-.9.9v5.85a.45.45 0 00.9 0V2.4h5.85a.45.45 0 000-.9H2.4zm1.8 1.8c-.5 0-.9.4-.9.9v5.4c0 .5.4.9.9.9h5.4c.5 0 .9-.4.9-.9V4.2c0-.5-.4-.9-.9-.9H4.2zm5.4.9H4.2v5.4h5.4V4.2z" fill="currentColor" fill-rule="evenodd"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF" data-item-id="17322316849"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" fill-rule="evenodd" d="M7.5774 10.2175c.2526.1731.574.3579.95.5005.7296.2765 1.2749.293 1.5271.2782.5622-.0317.6379-.3878.3361-.8304-.3444-.5044-.6761-1.0753-.6435-1.707.5348-.79.82-1.7222.8187-2.6761C10.5658 3.1413 8.4244 1 5.7829 1 3.1414 1 1 3.1413 1 5.7827c0 2.6413 2.1414 4.7827 4.783 4.7827a4.775 4.775 0 001.7944-.3479zm-1.7945-8.348a3.9134 3.9134 0 00-3.9133 3.9132 3.913 3.913 0 003.9133 3.913 3.899 3.899 0 001.6632-.3695.4348.4348 0 01.4495.0483c.2275.1743.55.3826.9401.5304.1696.0644.3244.1109.463.1439-.1447-.2639-.2912-.5782-.3582-.8739-.0696-.3052-.174-.8365.0287-1.12a3.8929 3.8929 0 00.727-2.2722 3.913 3.913 0 00-3.9133-3.9131z"></path><path fill="currentColor" d="M6.1665 8.2321a.5435.5435 0 10-.7686-.7686.5435.5435 0 00.7686.7686zM5.7822 4.0434c-.3988 0-.6957.2-.811.4191a.4348.4348 0 11-.77-.4034c.2874-.5483.91-.8853 1.581-.8853.8826 0 1.7392.6105 1.7392 1.5218 0 .7596-.5948 1.3104-1.3044 1.4726v.0492a.4347.4347 0 11-.8697 0v-.4348a.4348.4348 0 01.4349-.4348c.5578 0 .8696-.363.8696-.6522 0-.2891-.3118-.6522-.8696-.6522z"></path></svg></div><div class="spring--1fX2db"></div><div class="caption--4yIjjC"># 17322316849&nbsp;<span>{current_data}</span><span class="clock--3go1gx"></span><span>{current_time}</span></div></div><div class="coupon__content--23pZkK"><table class="coupon__table--5vgdP2"><thead><tr class="coupon__table-row--6OoyA1 _use_color_settings--SQwskl"><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_event--3MkqAt" colspan="2">Событие</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_stake--4UOCA4">Ставка</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_factor--13qGSb">Коэффициент</th></tr></thead><tbody class="coupon__table-body--6r9aPL"><tr class="coupon__table-row--6OoyA1"><td class="coupon__table-col--3p8NRM" colspan="2"><span class="coupon__sport-icon--4VDiOV _use_color_settings--SQwskl" style="background-image: url(&quot;//origin.by0e87-resources.by/ContentCommon/Logotypes/SportKinds/new-design/white_new/1-football.svg&quot;);"></span><a class="coupon__event-link--4XQ9ZP" href="/sports/football/90707/40594250/">{name_of_event}</a></td><td class="coupon__table-col--3p8NRM _type_stake--4UOCA4"><span>{stavka}</span></td><td class="coupon__table-col--3p8NRM coupon__table-status--77SBfz _type_factor-value--5U80LG _type_label--4DkPHs _status_none--6pMbDE" title=""><span class="coupon__table-stake--PyBpdc">{koef}</span></td></tr></tbody></table></div><div class="coupon__info--630O8g"><div class="coupon__info-head--6Vvxw5"><div class="coupon__info-item-inner--yZFTIb"><div class="coupon__info-item--7bN5Q9" title="Тип ставки"><i class="coupon__icon--3foYqw _type_info--4M4Sar _icon_info-black--3zl3SC"></i><i class="coupon__info-text--1McvPX">Одинар</i></div><div class="coupon__info-item--7bN5Q9" title="Общий коэффициент"><i class="icon--5s9fxK _icon_at-black--1tmMQN     coupon__icon--3foYqw _type_info--4M4Sar"></i><i class="coupon__info-text--1McvPX">{koef}</i></div></div><div class="coupon__info-item--7bN5Q9 _type_items--2iVOPQ _register--ggFmt0"><i class="coupon__icon--3foYqw _type_info--4M4Sar _type_win--3qGDku _icon_stake-win-black--4XfUCb"></i><i class="coupon__info-text--1McvPX base-amount--2mYDrF"><span>{value}</span>&nbsp;RUB</i><i class="icon--5s9fxK _icon_arrow-right-gray-2--7xYZ0l coupon__icon-arrow--4YvyJH"></i><i class="coupon__info-text--1McvPX win-amount--4pXoPH"><span style="display: inline-block;">{value_koef}</span>&nbsp;RUB</i></div></div><div></div></div><div class="coupon__sell--PKzHaK"><div class="coupon__sell-button-area--6ZRtWU"><a class="coupon__sell-button--7jyHSE"><span>Продать за </span><span class="coupon__sell-highlight--2Vqg1D">{Sell}&nbsp;RUB</span></a><a class="coupon__sell-switch--1wvFV4 _type_up--2VfeXJ _17322316849" title="При изменении суммы согласиться с повышением"></a></div></div></article></div>
                            <div class="separator--5ixw9J" style="height: 1px; background-color: rgb(37, 62, 91);"></div>
                        `;
            
                        // Найти элемент, после которого нужно вставить новый блок div
                        var targetElement = document.querySelector(".header--4VBxlj");
            
                        // Вставить новый блок div после целевого элемента
                        targetElement.insertAdjacentElement("afterend", div);
                        """

                        driver.execute_script(script2)

                        balance_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header__login-balance")))
                        balance_text = balance_element.text
                        balance = float(balance_text)
                        new_balance = balance - float(value2)
                        int(new_balance)
                        driver.execute_script("arguments[0].innerText = arguments[1]", balance_element, str(new_balance))

                        time.sleep(300)

                        class_name4 = "coupon--61Qt1m"
                        modal3 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "coupon--61Qt1m")))
                        script4 = f"var element = document.getElementsByClassName('{class_name4}')[0]; element.parentNode.removeChild(element);"
                        driver.execute_script(script4)

                        script5 = f"""
                                    var div = document.createElement("div");
                                    div.innerHTML = `
                                        <article class="coupon--61Qt1m"><div class="coupon__head--5nsL30"><div class="coupon__iconGeometry--4HFE4v svgDelete--4w0Fgk flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 15 15" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M3.46143 11.3242L11.4614 3.32422M3.46143 3.32422L11.4614 11.3242L3.46143 3.32422Z" stroke="currentColor"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M2.4 1.5c-.5 0-.9.4-.9.9v5.85a.45.45 0 00.9 0V2.4h5.85a.45.45 0 000-.9H2.4zm1.8 1.8c-.5 0-.9.4-.9.9v5.4c0 .5.4.9.9.9h5.4c.5 0 .9-.4.9-.9V4.2c0-.5-.4-.9-.9-.9H4.2zm5.4.9H4.2v5.4h5.4V4.2z" fill="currentColor" fill-rule="evenodd"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF" data-item-id="17337564226"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" fill-rule="evenodd" d="M7.5774 10.2175c.2526.1731.574.3579.95.5005.7296.2765 1.2749.293 1.5271.2782.5622-.0317.6379-.3878.3361-.8304-.3444-.5044-.6761-1.0753-.6435-1.707.5348-.79.82-1.7222.8187-2.6761C10.5658 3.1413 8.4244 1 5.7829 1 3.1414 1 1 3.1413 1 5.7827c0 2.6413 2.1414 4.7827 4.783 4.7827a4.775 4.775 0 001.7944-.3479zm-1.7945-8.348a3.9134 3.9134 0 00-3.9133 3.9132 3.913 3.913 0 003.9133 3.913 3.899 3.899 0 001.6632-.3695.4348.4348 0 01.4495.0483c.2275.1743.55.3826.9401.5304.1696.0644.3244.1109.463.1439-.1447-.2639-.2912-.5782-.3582-.8739-.0696-.3052-.174-.8365.0287-1.12a3.8929 3.8929 0 00.727-2.2722 3.913 3.913 0 00-3.9133-3.9131z"></path><path fill="currentColor" d="M6.1665 8.2321a.5435.5435 0 10-.7686-.7686.5435.5435 0 00.7686.7686zM5.7822 4.0434c-.3988 0-.6957.2-.811.4191a.4348.4348 0 11-.77-.4034c.2874-.5483.91-.8853 1.581-.8853.8826 0 1.7392.6105 1.7392 1.5218 0 .7596-.5948 1.3104-1.3044 1.4726v.0492a.4347.4347 0 11-.8697 0v-.4348a.4348.4348 0 01.4349-.4348c.5578 0 .8696-.363.8696-.6522 0-.2891-.3118-.6522-.8696-.6522z"></path></svg></div><div class="spring--1fX2db"></div><div class="caption--4yIjjC"># 17337564226&nbsp;<span>{current_data}</span><span class="clock--3go1gx"></span><span>{current_time}</span></div></div><div class="coupon__content--23pZkK"><table class="coupon__table--5vgdP2"><thead><tr class="coupon__table-row--6OoyA1 _use_color_settings--SQwskl"><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_event--3MkqAt" colspan="2">Событие</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_stake--4UOCA4">Исход</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_factor--13qGSb">Коэффициент</th></tr></thead><tbody class="coupon__table-body--6r9aPL"><tr class="coupon__table-row--6OoyA1"><td class="coupon__table-col--3p8NRM" colspan="2"><span class="coupon__sport-icon--4VDiOV _use_color_settings--SQwskl" style="background-image: url(&quot;//origin.bk6bba-resources.com/ContentCommon/Logotypes/SportKinds/new-design/white_new/1-football.svg&quot;);"></span><span class="coupon__table-border--2sNccJ"><span class="coupon__table-score--3X9mjO" title="Счет в момент заключения пари">3:1</span></span><span>{name_of_event}</span></td><td class="coupon__table-col--3p8NRM _type_stake--4UOCA4"><span>{stavka}</span></td><td class="coupon__table-col--3p8NRM coupon__table-status--77SBfz _type_factor-value--5U80LG _type_label--4DkPHs _status_win--3Wh23L" title="Пари сыграло.(3:1)"><span class="coupon__table-stake--PyBpdc">{koef}</span></td></tr></tbody></table></div><div class="coupon__info--630O8g"><div class="coupon__info-head--6Vvxw5"><div class="coupon__info-item-inner--yZFTIb"><div class="coupon__info-item--7bN5Q9" title="Тип пари"><i class="coupon__icon--3foYqw _type_info--4M4Sar _icon_info-black--3zl3SC"></i><i class="coupon__info-text--1McvPX">Одинар</i></div><div class="coupon__info-item--7bN5Q9" title="Общий коэффициент"><i class="icon--5s9fxK _icon_at-black--1tmMQN coupon__icon--3foYqw _type_info--4M4Sar"></i><i class="coupon__info-text--1McvPX">{koef}</i></div></div><div class="coupon__info-item--7bN5Q9 _type_items--2iVOPQ _win--5kWedI"><i class="coupon__icon--3foYqw _type_info--4M4Sar _type_win--3qGDku _icon_stake-win-orange--7qRZzw _status_win--3Wh23L"></i><i class="coupon__info-text--1McvPX base-amount--2mYDrF"><span>{value2}</span></i><i class="icon--5s9fxK _icon_arrow-right-gray-2--7xYZ0l coupon__icon-arrow--4YvyJH"></i><i class="coupon__info-text--1McvPX win-amount--4pXoPH"><span style="display: inline-block;">{value_koef}</span></i></div><div class="coupon__info-label--1NOYoS _style_win--98b3vW _style_colored--8dYqV3"><span>Выигрыш</span></div></div><div></div></div></article>
                                        <article class="coupon--61Qt1m"><div class="coupon__head--5nsL30"><div class="coupon__iconGeometry--4HFE4v svgDelete--4w0Fgk flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 15 15" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M3.46143 11.3242L11.4614 3.32422M3.46143 3.32422L11.4614 11.3242L3.46143 3.32422Z" stroke="currentColor"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M2.4 1.5c-.5 0-.9.4-.9.9v5.85a.45.45 0 00.9 0V2.4h5.85a.45.45 0 000-.9H2.4zm1.8 1.8c-.5 0-.9.4-.9.9v5.4c0 .5.4.9.9.9h5.4c.5 0 .9-.4.9-.9V4.2c0-.5-.4-.9-.9-.9H4.2zm5.4.9H4.2v5.4h5.4V4.2z" fill="currentColor" fill-rule="evenodd"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF" data-item-id="17337558396"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" fill-rule="evenodd" d="M7.5774 10.2175c.2526.1731.574.3579.95.5005.7296.2765 1.2749.293 1.5271.2782.5622-.0317.6379-.3878.3361-.8304-.3444-.5044-.6761-1.0753-.6435-1.707.5348-.79.82-1.7222.8187-2.6761C10.5658 3.1413 8.4244 1 5.7829 1 3.1414 1 1 3.1413 1 5.7827c0 2.6413 2.1414 4.7827 4.783 4.7827a4.775 4.775 0 001.7944-.3479zm-1.7945-8.348a3.9134 3.9134 0 00-3.9133 3.9132 3.913 3.913 0 003.9133 3.913 3.899 3.899 0 001.6632-.3695.4348.4348 0 01.4495.0483c.2275.1743.55.3826.9401.5304.1696.0644.3244.1109.463.1439-.1447-.2639-.2912-.5782-.3582-.8739-.0696-.3052-.174-.8365.0287-1.12a3.8929 3.8929 0 00.727-2.2722 3.913 3.913 0 00-3.9133-3.9131z"></path><path fill="currentColor" d="M6.1665 8.2321a.5435.5435 0 10-.7686-.7686.5435.5435 0 00.7686.7686zM5.7822 4.0434c-.3988 0-.6957.2-.811.4191a.4348.4348 0 11-.77-.4034c.2874-.5483.91-.8853 1.581-.8853.8826 0 1.7392.6105 1.7392 1.5218 0 .7596-.5948 1.3104-1.3044 1.4726v.0492a.4347.4347 0 11-.8697 0v-.4348a.4348.4348 0 01.4349-.4348c.5578 0 .8696-.363.8696-.6522 0-.2891-.3118-.6522-.8696-.6522z"></path></svg></div><div class="spring--1fX2db"></div><div class="caption--4yIjjC"># 17337558396&nbsp;<span>{current_data}</span><span class="clock--3go1gx"></span><span>{current_time}</span></div></div><div class="coupon__content--23pZkK"><table class="coupon__table--5vgdP2"><thead><tr class="coupon__table-row--6OoyA1 _use_color_settings--SQwskl"><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_event--3MkqAt" colspan="2">Событие</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_stake--4UOCA4">Исход</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_factor--13qGSb">Коэффициент</th></tr></thead><tbody class="coupon__table-body--6r9aPL"><tr class="coupon__table-row--6OoyA1"><td class="coupon__table-col--3p8NRM" colspan="2"><span class="coupon__sport-icon--4VDiOV _use_color_settings--SQwskl" style="background-image: url(&quot;//origin.bk6bba-resources.com/ContentCommon/Logotypes/SportKinds/new-design/white_new/1-football.svg&quot;);"></span><span class="coupon__table-border--2sNccJ"><span class="coupon__table-score--3X9mjO" title="Счет в момент заключения пари">3:1</span></span><span>{name_of_event}</span></td><td class="coupon__table-col--3p8NRM _type_stake--4UOCA4"><span>{stavka}</span></td><td class="coupon__table-col--3p8NRM coupon__table-status--77SBfz _type_factor-value--5U80LG _type_label--4DkPHs _status_lose--h4Xx4x" title="Пари не сыграло. (3:1)"><span class="coupon__table-stake--PyBpdc">{koef}</span></td></tr></tbody></table></div><div class="coupon__info--630O8g"><div class="coupon__info-head--6Vvxw5"><div class="coupon__info-item-inner--yZFTIb"><div class="coupon__info-item--7bN5Q9" title="Тип пари"><i class="coupon__icon--3foYqw _type_info--4M4Sar _icon_info-black--3zl3SC"></i><i class="coupon__info-text--1McvPX">Одинар</i></div><div class="coupon__info-item--7bN5Q9" title="Общий коэффициент"><i class="icon--5s9fxK _icon_at-black--1tmMQN coupon__icon--3foYqw _type_info--4M4Sar"></i><i class="coupon__info-text--1McvPX">{koef}</i></div></div><div class="coupon__info-item--7bN5Q9 _type_items--2iVOPQ _lose--7bkdvA _withoutWinAmount--erLpry"><i class="coupon__icon--3foYqw _type_info--4M4Sar _type_win--3qGDku _icon-coupon-lose--8t9QrS"></i><i class="coupon__info-text--1McvPX base-amount--2mYDrF"><span>{value2}</span></i></div><div class="coupon__info-label--1NOYoS _style_loose--46YakN _style_colored--8dYqV3"><span>Проигрыш</span></div></div><div></div></div></article>
                                        
                                    `;
            
                                    // Найти элемент, после которого нужно вставить новый блок div
                                    var targetElement = document.querySelector(".separator--5ixw9J");
            
                                    // Вставить новый блок div после целевого элемента
                                    targetElement.insertAdjacentElement("afterend", div);
                                    """

                        driver.execute_script(script5)

                    else:
                        element_with_class1 = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "event-data--1UykiN")))
                        for i in element_with_class1:
                            name_of_events.append(i.text)

                        element_with_class2 = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "v-current--6su1Qn")))
                        for i in element_with_class2:
                            koefs.append(i.text)

                        element_with_class3 = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "column3--1r5hIk")))
                        for i in element_with_class3:
                            stavki.append(i.text)
                        stavki.pop(0)

                        input_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sum-panel__input--5a9SqV")))
                        value = input_element.get_attribute("value")
                        value2 = value
                        product = 1

                        for koef in koefs:
                            product = product * float(koef)
                        product =round(product, 2)

                        valuekoef = float(value2) * float(product)
                        value_koef = round(valuekoef, 2)

                        class_name2 = "new-coupon--5cY6lQ"
                        modal1 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new-coupon--5cY6lQ")))
                        script1 = f"var element = document.getElementsByClassName('{class_name2}')[0]; element.parentNode.removeChild(element);"
                        driver.execute_script(script1)

                        script2 = f"""
                                                var div = document.createElement("div");
                                                div.innerHTML = `
                                                    <div class="new-coupon--5cY6lQ" style="background-color: rgb(37, 62, 91);"><div class="empty--4pI7r2" style="background-color: rgb(37, 62, 91);"><span class="caption-area--6Yqezu">Выберите исход события, чтобы заключить пари</span><div class="switch-area--IywgSo"><span class="switch--1HvPTt _use_color_settings--2h94AH _off--4i6Yy3"></span><span class="text--2D5yKe"><span style="cursor: pointer;">Пари в один клик</span></span></div><div style="height: 16px;"></div></div><div class="separator--5ixw9J" style="height: 1px; background-color: rgb(37, 62, 91);"></div></div>
                                                    <div class="coupon-list--UluSeE _top-padding--6VyvQR" style="background-color: rgb(37, 62, 91);"><article class="coupon--61Qt1m"><div class="coupon__head--5nsL30"><div class="coupon__iconGeometry--4HFE4v svgDelete--4w0Fgk flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 15 15" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M3.46143 11.3242L11.4614 3.32422M3.46143 3.32422L11.4614 11.3242L3.46143 3.32422Z" stroke="currentColor"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M2.4 1.5c-.5 0-.9.4-.9.9v5.85a.45.45 0 00.9 0V2.4h5.85a.45.45 0 000-.9H2.4zm1.8 1.8c-.5 0-.9.4-.9.9v5.4c0 .5.4.9.9.9h5.4c.5 0 .9-.4.9-.9V4.2c0-.5-.4-.9-.9-.9H4.2zm5.4.9H4.2v5.4h5.4V4.2z" fill="currentColor" fill-rule="evenodd"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF" data-item-id="17322316849"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" fill-rule="evenodd" d="M7.5774 10.2175c.2526.1731.574.3579.95.5005.7296.2765 1.2749.293 1.5271.2782.5622-.0317.6379-.3878.3361-.8304-.3444-.5044-.6761-1.0753-.6435-1.707.5348-.79.82-1.7222.8187-2.6761C10.5658 3.1413 8.4244 1 5.7829 1 3.1414 1 1 3.1413 1 5.7827c0 2.6413 2.1414 4.7827 4.783 4.7827a4.775 4.775 0 001.7944-.3479zm-1.7945-8.348a3.9134 3.9134 0 00-3.9133 3.9132 3.913 3.913 0 003.9133 3.913 3.899 3.899 0 001.6632-.3695.4348.4348 0 01.4495.0483c.2275.1743.55.3826.9401.5304.1696.0644.3244.1109.463.1439-.1447-.2639-.2912-.5782-.3582-.8739-.0696-.3052-.174-.8365.0287-1.12a3.8929 3.8929 0 00.727-2.2722 3.913 3.913 0 00-3.9133-3.9131z"></path><path fill="currentColor" d="M6.1665 8.2321a.5435.5435 0 10-.7686-.7686.5435.5435 0 00.7686.7686zM5.7822 4.0434c-.3988 0-.6957.2-.811.4191a.4348.4348 0 11-.77-.4034c.2874-.5483.91-.8853 1.581-.8853.8826 0 1.7392.6105 1.7392 1.5218 0 .7596-.5948 1.3104-1.3044 1.4726v.0492a.4347.4347 0 11-.8697 0v-.4348a.4348.4348 0 01.4349-.4348c.5578 0 .8696-.363.8696-.6522 0-.2891-.3118-.6522-.8696-.6522z"></path></svg></div><div class="spring--1fX2db"></div><div class="caption--4yIjjC"># 17322316849&nbsp;<span>{current_data}</span><span class="clock--3go1gx"></span><span>{current_time}</span></div></div><div class="coupon__content--23pZkK"><table class="coupon__table--5vgdP2"><thead><tr class="coupon__table-row--6OoyA1 _use_color_settings--SQwskl"><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_event--3MkqAt" colspan="2">Событие</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_stake--4UOCA4">Ставка</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_factor--13qGSb">Коэффициент</th></tr></thead><tbody class="coupon__table-body--6r9aPL"><tr class="coupon__table-row--6OoyA1"><td class="coupon__table-col--3p8NRM" colspan="2"><span class="coupon__sport-icon--4VDiOV _use_color_settings--SQwskl" style="background-image: url(&quot;//origin.by0e87-resources.by/ContentCommon/Logotypes/SportKinds/new-design/white_new/1-football.svg&quot;);"></span><a class="coupon__event-link--4XQ9ZP" href="/sports/football/90707/40594250/">{name_of_events[0]}</a></td><td class="coupon__table-col--3p8NRM _type_stake--4UOCA4"><span>{stavki[0]}</span></td><td class="coupon__table-col--3p8NRM coupon__table-status--77SBfz _type_factor-value--5U80LG _type_label--4DkPHs _status_none--6pMbDE" title=""><span class="coupon__table-stake--PyBpdc">{koef[0]}</span></td></tr></tbody></table></div><div class="coupon__info--630O8g"><div class="coupon__info-head--6Vvxw5"><div class="coupon__info-item-inner--yZFTIb"><div class="coupon__info-item--7bN5Q9" title="Тип ставки"><i class="coupon__icon--3foYqw _type_info--4M4Sar _icon_info-black--3zl3SC"></i><i class="coupon__info-text--1McvPX">Экспресс</i></div><div class="coupon__info-item--7bN5Q9" title="Общий коэффициент"><i class="icon--5s9fxK _icon_at-black--1tmMQN     coupon__icon--3foYqw _type_info--4M4Sar"></i><i class="coupon__info-text--1McvPX">{product}</i></div></div><div class="coupon__info-item--7bN5Q9 _type_items--2iVOPQ _register--ggFmt0"><i class="coupon__icon--3foYqw _type_info--4M4Sar _type_win--3qGDku _icon_stake-win-black--4XfUCb"></i><i class="coupon__info-text--1McvPX base-amount--2mYDrF"><span>{value}</span>&nbsp;RUB</i><i class="icon--5s9fxK _icon_arrow-right-gray-2--7xYZ0l coupon__icon-arrow--4YvyJH"></i><i class="coupon__info-text--1McvPX win-amount--4pXoPH"><span style="display: inline-block;">{value_koef}</span>&nbsp;RUB</i></div></div><div></div></div></article></div>
                                                    <div class="separator--5ixw9J" style="height: 1px; background-color: rgb(37, 62, 91);"></div>
                                                `;

                                                // Найти элемент, после которого нужно вставить новый блок div
                                                var targetElement = document.querySelector(".header--4VBxlj");

                                                // Вставить новый блок div после целевого элемента
                                                targetElement.insertAdjacentElement("afterend", div);
                                                """

                        driver.execute_script(script2)

                        for i in range(count-1, 0, -1):
                            script_2 = f"""
                                var code = `
                                    <tr class="coupon__table-row--6OoyA1">
                                        <td class="coupon__table-col--3p8NRM" colspan="2">
                                            <span class="coupon__sport-icon--4VDiOV _use_color_settings--SQwskl" style="background-image: url(&quot;//origin.by0e87-resources.by/ContentCommon/Logotypes/SportKinds/new-design/white_new/1-football.svg&quot;);"></span>
                                            <a class="coupon__event-link--4XQ9ZP" href="/sports/football/90707/40594250/">{name_of_events[i]}</a>
                                        </td>
                                        <td class="coupon__table-col--3p8NRM _type_stake--4UOCA4">
                                            <span>{stavki[i]}</span>
                                        </td>
                                        <td class="coupon__table-col--3p8NRM coupon__table-status--77SBfz _type_factor-value--5U80LG _type_label--4DkPHs _status_none--6pMbDE" title="">
                                            <span class="coupon__table-stake--PyBpdc">{koefs[i]}</span>
                                        </td>
                                    </tr>
                                `;
                                var tbody = document.createElement("tbody");
                                tbody.classList.add("coupon__table-body--6r9aPL");
                                tbody.innerHTML = code;

                                // Найти элемент, после которого нужно вставить новый блок tbody
                                var targetElement = document.querySelector(".coupon__table-body--6r9aPL");

                                // Вставить новый блок tbody после целевого элемента
                                targetElement.insertAdjacentElement("afterend", tbody);
                            """

                            driver.execute_script(script_2)

                        balance_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header__login-balance")))
                        balance_text = balance_element.text
                        balance = float(balance_text)
                        new_balance = balance - float(value2)
                        int(new_balance)
                        driver.execute_script("arguments[0].innerText = arguments[1]", balance_element, str(new_balance))

                        time.sleep(300)

                        class_name4 = "coupon--61Qt1m"
                        modal3 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "coupon--61Qt1m")))
                        script4 = f"var element = document.getElementsByClassName('{class_name4}')[0]; element.parentNode.removeChild(element);"
                        driver.execute_script(script4)

                        script5 = f"""
                                    var div = document.createElement("div");
                                    div.innerHTML = `
                                        <article class="coupon--61Qt1m"><div class="coupon__head--5nsL30"><div class="coupon__iconGeometry--4HFE4v svgDelete--4w0Fgk flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 15 15" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M3.46143 11.3242L11.4614 3.32422M3.46143 3.32422L11.4614 11.3242L3.46143 3.32422Z" stroke="currentColor"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M2.4 1.5c-.5 0-.9.4-.9.9v5.85a.45.45 0 00.9 0V2.4h5.85a.45.45 0 000-.9H2.4zm1.8 1.8c-.5 0-.9.4-.9.9v5.4c0 .5.4.9.9.9h5.4c.5 0 .9-.4.9-.9V4.2c0-.5-.4-.9-.9-.9H4.2zm5.4.9H4.2v5.4h5.4V4.2z" fill="currentColor" fill-rule="evenodd"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF" data-item-id="17337564226"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" fill-rule="evenodd" d="M7.5774 10.2175c.2526.1731.574.3579.95.5005.7296.2765 1.2749.293 1.5271.2782.5622-.0317.6379-.3878.3361-.8304-.3444-.5044-.6761-1.0753-.6435-1.707.5348-.79.82-1.7222.8187-2.6761C10.5658 3.1413 8.4244 1 5.7829 1 3.1414 1 1 3.1413 1 5.7827c0 2.6413 2.1414 4.7827 4.783 4.7827a4.775 4.775 0 001.7944-.3479zm-1.7945-8.348a3.9134 3.9134 0 00-3.9133 3.9132 3.913 3.913 0 003.9133 3.913 3.899 3.899 0 001.6632-.3695.4348.4348 0 01.4495.0483c.2275.1743.55.3826.9401.5304.1696.0644.3244.1109.463.1439-.1447-.2639-.2912-.5782-.3582-.8739-.0696-.3052-.174-.8365.0287-1.12a3.8929 3.8929 0 00.727-2.2722 3.913 3.913 0 00-3.9133-3.9131z"></path><path fill="currentColor" d="M6.1665 8.2321a.5435.5435 0 10-.7686-.7686.5435.5435 0 00.7686.7686zM5.7822 4.0434c-.3988 0-.6957.2-.811.4191a.4348.4348 0 11-.77-.4034c.2874-.5483.91-.8853 1.581-.8853.8826 0 1.7392.6105 1.7392 1.5218 0 .7596-.5948 1.3104-1.3044 1.4726v.0492a.4347.4347 0 11-.8697 0v-.4348a.4348.4348 0 01.4349-.4348c.5578 0 .8696-.363.8696-.6522 0-.2891-.3118-.6522-.8696-.6522z"></path></svg></div><div class="spring--1fX2db"></div><div class="caption--4yIjjC"># 17337564226&nbsp;<span>{current_data}</span><span class="clock--3go1gx"></span><span>{current_time}</span></div></div><div class="coupon__content--23pZkK"><table class="coupon__table--5vgdP2"><thead><tr class="coupon__table-row--6OoyA1 _use_color_settings--SQwskl"><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_event--3MkqAt" colspan="2">Событие</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_stake--4UOCA4">Исход</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_factor--13qGSb">Коэффициент</th></tr></thead><tbody class="coupon__table-body--6r9aPL"><tr class="coupon__table-row--6OoyA1"><td class="coupon__table-col--3p8NRM" colspan="2"><span class="coupon__sport-icon--4VDiOV _use_color_settings--SQwskl" style="background-image: url(&quot;//origin.bk6bba-resources.com/ContentCommon/Logotypes/SportKinds/new-design/white_new/1-football.svg&quot;);"></span><span class="coupon__table-border--2sNccJ"><span class="coupon__table-score--3X9mjO" title="Счет в момент заключения пари">3:1</span></span><span>{name_of_events[0]}</span></td><td class="coupon__table-col--3p8NRM _type_stake--4UOCA4"><span>{stavki[0]}</span></td><td class="coupon__table-col--3p8NRM coupon__table-status--77SBfz _type_factor-value--5U80LG _type_label--4DkPHs _status_win--3Wh23L" title="Пари сыграло.(3:1)"><span class="coupon__table-stake--PyBpdc">{koefs[0]}</span></td></tr></tbody></table></div><div class="coupon__info--630O8g"><div class="coupon__info-head--6Vvxw5"><div class="coupon__info-item-inner--yZFTIb"><div class="coupon__info-item--7bN5Q9" title="Тип пари"><i class="coupon__icon--3foYqw _type_info--4M4Sar _icon_info-black--3zl3SC"></i><i class="coupon__info-text--1McvPX">Экспресс</i></div><div class="coupon__info-item--7bN5Q9" title="Общий коэффициент"><i class="icon--5s9fxK _icon_at-black--1tmMQN coupon__icon--3foYqw _type_info--4M4Sar"></i><i class="coupon__info-text--1McvPX">{product}</i></div></div><div class="coupon__info-item--7bN5Q9 _type_items--2iVOPQ _win--5kWedI"><i class="coupon__icon--3foYqw _type_info--4M4Sar _type_win--3qGDku _icon_stake-win-orange--7qRZzw _status_win--3Wh23L"></i><i class="coupon__info-text--1McvPX base-amount--2mYDrF"><span>{value2}</span></i><i class="icon--5s9fxK _icon_arrow-right-gray-2--7xYZ0l coupon__icon-arrow--4YvyJH"></i><i class="coupon__info-text--1McvPX win-amount--4pXoPH"><span style="display: inline-block;">{value_koef}</span></i></div><div class="coupon__info-label--1NOYoS _style_win--98b3vW _style_colored--8dYqV3"><span>Выигрыш</span></div></div><div></div></div></article>
                            
                                    `;
            
                                    // Найти элемент, после которого нужно вставить новый блок div
                                    var targetElement = document.querySelector(".separator--5ixw9J");
            
                                    // Вставить новый блок div после целевого элемента
                                    targetElement.insertAdjacentElement("afterend", div);
                                    """
                        driver.execute_script(script5)

                        for i in range(count-1, 0, -1):
                            script_5 = f"""
                                var code = `<tr class="coupon__table-row--6OoyA1"><td class="coupon__table-col--3p8NRM" colspan="2"><span class="coupon__sport-icon--4VDiOV _use_color_settings--SQwskl" style="background-image: url(&quot;//origin.bk6bba-resources.com/ContentCommon/Logotypes/SportKinds/new-design/white_new/1-football.svg&quot;);"></span><span class="coupon__table-border--2sNccJ"><span class="coupon__table-score--3X9mjO" title="Счет в момент заключения пари">3:1</span></span><span>{name_of_events[i]}</span></td><td class="coupon__table-col--3p8NRM _type_stake--4UOCA4"><span>{stavki[i]}</span></td><td class="coupon__table-col--3p8NRM coupon__table-status--77SBfz _type_factor-value--5U80LG _type_label--4DkPHs _status_win--3Wh23L" title="Пари сыграло.(3:1)"><span class="coupon__table-stake--PyBpdc">{koefs[i]}</span></td></tr>
                                    
                                `;
                                var tbody = document.createElement("tbody");
                                tbody.classList.add("coupon__table-body--6r9aPL");
                                tbody.innerHTML = code;

                                // Найти элемент, после которого нужно вставить новый блок tbody
                                var targetElement = document.querySelector(".coupon__table-body--6r9aPL");

                                // Вставить новый блок tbody после целевого элемента
                                targetElement.insertAdjacentElement("afterend", tbody);
                            """

                            driver.execute_script(script_5)

                        script6 = f"""
                                                            var div = document.createElement("div");
                                                            div.innerHTML = `
                                                                <article class="coupon--61Qt1m"><div class="coupon__head--5nsL30"><div class="coupon__iconGeometry--4HFE4v svgDelete--4w0Fgk flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 15 15" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M3.46143 11.3242L11.4614 3.32422M3.46143 3.32422L11.4614 11.3242L3.46143 3.32422Z" stroke="currentColor"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M2.4 1.5c-.5 0-.9.4-.9.9v5.85a.45.45 0 00.9 0V2.4h5.85a.45.45 0 000-.9H2.4zm1.8 1.8c-.5 0-.9.4-.9.9v5.4c0 .5.4.9.9.9h5.4c.5 0 .9-.4.9-.9V4.2c0-.5-.4-.9-.9-.9H4.2zm5.4.9H4.2v5.4h5.4V4.2z" fill="currentColor" fill-rule="evenodd"></path></svg></div><div class="coupon__iconGeometry--4HFE4v coupon__iconColorHover--2osOkf flexWrap--3Rg9Vk clickable--4LdpSF" data-item-id="17337558396"><svg class="" height="12" viewBox="0 0 12 12" width="12" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" fill-rule="evenodd" d="M7.5774 10.2175c.2526.1731.574.3579.95.5005.7296.2765 1.2749.293 1.5271.2782.5622-.0317.6379-.3878.3361-.8304-.3444-.5044-.6761-1.0753-.6435-1.707.5348-.79.82-1.7222.8187-2.6761C10.5658 3.1413 8.4244 1 5.7829 1 3.1414 1 1 3.1413 1 5.7827c0 2.6413 2.1414 4.7827 4.783 4.7827a4.775 4.775 0 001.7944-.3479zm-1.7945-8.348a3.9134 3.9134 0 00-3.9133 3.9132 3.913 3.913 0 003.9133 3.913 3.899 3.899 0 001.6632-.3695.4348.4348 0 01.4495.0483c.2275.1743.55.3826.9401.5304.1696.0644.3244.1109.463.1439-.1447-.2639-.2912-.5782-.3582-.8739-.0696-.3052-.174-.8365.0287-1.12a3.8929 3.8929 0 00.727-2.2722 3.913 3.913 0 00-3.9133-3.9131z"></path><path fill="currentColor" d="M6.1665 8.2321a.5435.5435 0 10-.7686-.7686.5435.5435 0 00.7686.7686zM5.7822 4.0434c-.3988 0-.6957.2-.811.4191a.4348.4348 0 11-.77-.4034c.2874-.5483.91-.8853 1.581-.8853.8826 0 1.7392.6105 1.7392 1.5218 0 .7596-.5948 1.3104-1.3044 1.4726v.0492a.4347.4347 0 11-.8697 0v-.4348a.4348.4348 0 01.4349-.4348c.5578 0 .8696-.363.8696-.6522 0-.2891-.3118-.6522-.8696-.6522z"></path></svg></div><div class="spring--1fX2db"></div><div class="caption--4yIjjC"># 17337558396&nbsp;<span>{current_data}</span><span class="clock--3go1gx"></span><span>{current_time}</span></div></div><div class="coupon__content--23pZkK"><table class="coupon__table--5vgdP2"><thead><tr class="coupon__table-row--6OoyA1 _use_color_settings--SQwskl"><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_event--3MkqAt" colspan="2">Событие</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_stake--4UOCA4">Исход</th><th class="coupon__table-col--3p8NRM _type_head--4GKkz1 _type_factor--13qGSb">Коэффициент</th></tr></thead><tbody class="coupon__table-body--6r9aPL"><tr class="coupon__table-row--6OoyA1"><td class="coupon__table-col--3p8NRM" colspan="2"><span class="coupon__sport-icon--4VDiOV _use_color_settings--SQwskl" style="background-image: url(&quot;//origin.bk6bba-resources.com/ContentCommon/Logotypes/SportKinds/new-design/white_new/1-football.svg&quot;);"></span><span class="coupon__table-border--2sNccJ"><span class="coupon__table-score--3X9mjO" title="Счет в момент заключения пари">3:1</span></span><span>{name_of_events[0]}</span></td><td class="coupon__table-col--3p8NRM _type_stake--4UOCA4"><span>{stavki[0]}</span></td><td class="coupon__table-col--3p8NRM coupon__table-status--77SBfz _type_factor-value--5U80LG _type_label--4DkPHs _status_lose--h4Xx4x" title="Пари не сыграло. (3:1)"><span class="coupon__table-stake--PyBpdc">{koefs[0]}</span></td></tr></tbody></table></div><div class="coupon__info--630O8g"><div class="coupon__info-head--6Vvxw5"><div class="coupon__info-item-inner--yZFTIb"><div class="coupon__info-item--7bN5Q9" title="Тип пари"><i class="coupon__icon--3foYqw _type_info--4M4Sar _icon_info-black--3zl3SC"></i><i class="coupon__info-text--1McvPX">Экспресс</i></div><div class="coupon__info-item--7bN5Q9" title="Общий коэффициент"><i class="icon--5s9fxK _icon_at-black--1tmMQN coupon__icon--3foYqw _type_info--4M4Sar"></i><i class="coupon__info-text--1McvPX">{product}</i></div></div><div class="coupon__info-item--7bN5Q9 _type_items--2iVOPQ _lose--7bkdvA _withoutWinAmount--erLpry"><i class="coupon__icon--3foYqw _type_info--4M4Sar _type_win--3qGDku _icon-coupon-lose--8t9QrS"></i><i class="coupon__info-text--1McvPX base-amount--2mYDrF"><span>{value2}</span></i></div><div class="coupon__info-label--1NOYoS _style_loose--46YakN _style_colored--8dYqV3"><span>Проигрыш</span></div></div><div></div></div></article>
          
                                                            `;

                                                            // Найти элемент, после которого нужно вставить новый блок div
                                                            var targetElement = document.querySelector(".separator--5ixw9J");

                                                            // Вставить новый блок div после целевого элемента
                                                            targetElement.insertAdjacentElement("afterend", div);
                                                            """
                        driver.execute_script(script6)

                        for i in range(count-1, 0, -1):
                            script_6 = f"""
                                var code = `<tr class="coupon__table-row--6OoyA1"><td class="coupon__table-col--3p8NRM" colspan="2"><span class="coupon__sport-icon--4VDiOV _use_color_settings--SQwskl" style="background-image: url(&quot;//origin.bk6bba-resources.com/ContentCommon/Logotypes/SportKinds/new-design/white_new/1-football.svg&quot;);"></span><span class="coupon__table-border--2sNccJ"><span class="coupon__table-score--3X9mjO" title="Счет в момент заключения пари">3:1</span></span><span>{name_of_events[i]}</span></td><td class="coupon__table-col--3p8NRM _type_stake--4UOCA4"><span>{stavki[i]}</span></td><td class="coupon__table-col--3p8NRM coupon__table-status--77SBfz _type_factor-value--5U80LG _type_label--4DkPHs _status_win--3Wh23L" title="Пари сыграло.(3:1)"><span class="coupon__table-stake--PyBpdc">{koefs[i]}</span></td></tr>

                                `;
                                var tbody = document.createElement("tbody");
                                tbody.classList.add("coupon__table-body--6r9aPL");
                                tbody.innerHTML = code;

                                // Найти элемент, после которого нужно вставить новый блок tbody
                                var targetElement = document.querySelector(".coupon__table-body--6r9aPL");

                                // Вставить новый блок tbody после целевого элемента
                                targetElement.insertAdjacentElement("afterend", tbody);
                            """

                            driver.execute_script(script_6)




                except:
                    print("Не найден ")








