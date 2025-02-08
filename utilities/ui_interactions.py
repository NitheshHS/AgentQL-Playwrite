from utilities.logger import Logger


class UiInteractions(object):

    def __init__(self, page):
        self.logger=Logger()
        self.page=page

    def click_on_element(self, element):
        if element:
            self.logger.info(f'clicking {element}')
            element.click()
        else:
            self.logger.error('element not found')
            raise ValueError('element not found')

    def fill_element(self, element, text):
        if element:
            self.logger.info(f'filling {text} for element {element}')
            element.fill(text)
        else:
            self.logger.error('element not found')
            raise ValueError('element not found')

    def select_dropdown_by_value(self, dropdown_selector, value):
        if dropdown_selector:
            self.logger.info(f'selecting {dropdown_selector} of value {value}')
            dropdown_selector.select_option(value=value)
        else:
            self.logger.error('value not found')
            raise ValueError('value not found')

    def select_dropdown_by_label(self, dropdown_selector, label):
        if dropdown_selector:
            self.logger.info(f'selecting {dropdown_selector} of label {label}')
            dropdown_selector.select_option(label=label)
        else:
            self.logger.error('value not found')
            raise ValueError('value not found')

    def select_dropdown_by_index(self, dropdown_selector, index):
        if dropdown_selector:
            self.logger.info(f'selecting {dropdown_selector} of index {index}')
            dropdown_selector.select_option(index=index)
        else:
            self.logger.error('value not found')
            raise ValueError('value not found')




