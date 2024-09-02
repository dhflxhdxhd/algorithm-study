/*
CART_PRODUCTS 장바구니에 담긴 상품 정보
ID, CART_ID, NAME, PRICE

우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회

[결과]
CART_ID asc
*/
SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('Milk', 'Yogurt')
GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME) = 2;
