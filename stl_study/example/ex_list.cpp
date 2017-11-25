#include <iostream>
#include <list>
using namespace std;
  
struct Item
{
    Item(int itemCode, int buyMoney)
    {
        ItemCode = itemCode;
        BuyMoney = buyMoney;
    }

    int ItemCode; // 아이템 코드
    int BuyMoney; // 판매 금액
};

int main()
{
    list<Item> Itemlist;

    Item item1(1, 20000);
    Itemlist.push_front(item1);

    Item item2(2, 1000);
    Itemlist.push_front(item2);

    Item item3(3, 3000);
    Itemlist.push_back(item3);

    Item item4(4, 4500);
    Itemlist.push_back(item4);

    list<Item>::iterator iterEnd = Itemlist.end();
    for(list<Item>::iterator iterPos; iterPos != iterEnd; ++iterPos)
    {
        cout << "Item Code : " << iterPos->ItemCode << endl;
    }
    // stdout : 2 -> 1 -> 3 -> 4

    Itemlist.pop_front();

    Item front_item = Itemlist.front();
    cout << "Item code : " << front_item.ItemCode << endl;
    // stdout : 1

    Itemlist.pop_back();

    Item back_item = Itemlist.back();
    cout << "Item code : " << back_item.ItemCode << endl;
    // stdout : 3

    if(false == Itemlist.empty())
    {
        list<Item>::size_type Count = Itemlist.size();
        cout << "left cnt : " << Count << endl;
    }
    // stdout : 2

    Itemlist.clear();
    list<Item>::size_type Count = Itemlist.size();
    cout << "left cnt : " << Count << endl;
    // 0

} 