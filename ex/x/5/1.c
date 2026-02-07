int maxProfit(int* prices, int pricesSize) {
    int max_profit = 0;
    int buy_price = prices[0];
    int day;
    for (day=1; day < prices.; day++):
        if (buy_price > prices[day]){
            buy_price = prices[day];}
        else if (max_profit < prices[day] - buy_price){
            max_profit = prices[day] - buy_price;}
    return max_profit;
}