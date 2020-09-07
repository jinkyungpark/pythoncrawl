from scrapy.exceptions import DropItem


class Gmarket2Pipeline:

    # item : Item으로 작성한 것들이 하나하나 통과하게 되는 것
    def process_item(self, item, spider):
        # print("pipeline", item)
        if int(item["price"]) > 10000:
            return item
        else:
            raise DropItem("가격이 10,000보다 적음")
