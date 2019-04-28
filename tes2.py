from nsepy import get_history
from datetime import date
import matplotlib.pyplot as plt

stock_opt = get_history(symbol="ZEEL",
start=date(2019,3,1),
end=date(2019,4,2),
option_type="CE",
strike_price=450,
expiry_date=date(2019,4,25))

stock_opt.plot()
plt.show()


# zeel_option = get_history(symbol="ZEEL", start=date(2019,3,1), end=date(2019,4,2), index=False, futures=False, option_type="CE",
#                     expiry_date =date(2019,4,25), strike_price=450, series='EQ')
#
# zeel_option.plot()
# plt.show()