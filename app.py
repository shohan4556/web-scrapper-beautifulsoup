import wlog
import wscrap


wlog.set_custom_loggin('html/error4.log')


my_scrapper = wscrap.Scrapper(wscrap.url, wlog)

my_scrapper.retrive_webpage()
my_scrapper.write_webpage_as_html()
my_scrapper.read_webpage_from_html()
my_scrapper.convert_data_to_bs4()
my_scrapper.parse_soup_to_simple_html()
#my_scrapper.print_data()


