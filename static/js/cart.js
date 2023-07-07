new Vue({
    el: "#app",
    data: {
      products: [
        {
          image: "https://via.placeholder.com/200x150",
          name: "PRODUCT ITEM NUMBER 1",
          description: "Description for product item number 1",
          price: 5.99,
          quantity: 2
        },
        {
          image: "https://via.placeholder.com/200x150",
          name: "PRODUCT ITEM NUMBER 2",
          description: "Description for product item number 1",
          price: 9.99,
          quantity: 1
        }
      ],
      tax: 5,
      promotions: [
        {
          code: "SUMMER",
          discount: "50%"
        },
        {
          code: "AUTUMN",
          discount: "40%"
        },
        {
          code: "WINTER",
          discount: "30%"
        }
      ],
      promoCode: "",
      discount: 0
    },
    computed: {
      itemCount: function() {
        var count = 0;
  
        for (var i = 0; i < this.products.length; i++) {
          count += parseInt(this.products[i].quantity) || 0;
        }
  
        return count;
      },
      subTotal: function() {
        var subTotal = 0;
  
        for (var i = 0; i < this.products.length; i++) {
          subTotal += this.products[i].quantity * this.products[i].price;
        }
  
        return subTotal;
      },
      discountPrice: function() {
        return this.subTotal * this.discount / 100;
      },
      totalPrice: function() {
        return this.subTotal - this.discountPrice + this.tax;
      }
    },
    filters: {
      currencyFormatted: function(value) {
        return Number(value).toLocaleString("en-US", {
          style: "currency",
          currency: "INR"
        });
      }
    },
    methods: {
      updateQuantity: function(index, event) {
        var product = this.products[index];
        var value = event.target.value;
        var valueInt = parseInt(value);
  
        // Minimum quantity is 1, maximum quantity is 100, can left blank to input easily
        if (value === "") {
          product.quantity = value;
        } else if (valueInt > 0 && valueInt < 100) {
          product.quantity = valueInt;
        }
  
        this.$set(this.products, index, product);
      },
      checkQuantity: function(index, event) {
        // Update quantity to 1 if it is empty
        if (event.target.value === "") {
          var product = this.products[index];
          product.quantity = 1;
          this.$set(this.products, index, product);
        }
      },
      removeItem: function(index) {
        this.products.splice(index, 1);
      },
      checkPromoCode: function() {
        for (var i = 0; i < this.promotions.length; i++) {
          if (this.promoCode === this.promotions[i].code) {
            this.discount = parseFloat(
              this.promotions[i].discount.replace("%", "")
            );
            return;
          }
        }
  
        alert("Sorry, the Promotional code you entered is not valid!");
      }
    }
  });
  

  var removedItem,
  sum = 0;
  
  $(function(){
  // calculate the values at the start
  calculatePrices();
  
  // Click to remove an item
  $(document).on("click", "a.remove", function() {
    removeItem.apply(this);
  });
  
  // Undo removal link click
  $(document).on("click", ".removeAlert a", function(){    
  // insert it into the table
  addItemBackIn();
  //remove the removal alert message
  hideRemoveAlert();
  });
  
  $(document).on("change", "input.quantity", function(){
  var val = $(this).val(),
      pricePer,
      total
  
  if ( val <= "0") {
    removeItem.apply(this);
  } else {
    // reset the prices
    sum = 0;
    
    // get the price for the item
    pricePer = $(this).parents("td").prev("td").text();
    // set the pricePer to a nice, digestable number
    pricePer = formatNum(pricePer);
    // calculate the new total
    total = parseFloat(val * pricePer).toFixed(2);
    // set the total cell to the new price
    $(this).parents("td").siblings(".itemTotal").text("₹" + total);
    
    // recalculate prices for all items
    calculatePrices();
  }
  });
  
  });
  
  
  function removeItem() {
  // store the html
  removedItem = $(this).closest("tr").clone();
  // fade out the item row
  $(this).closest("tr").fadeOut(500, function() {
  $(this).remove();
  sum = 0;
  calculatePrices();
  });
  // fade in the removed confirmation alert
  $(".removeAlert").fadeIn();
  
  // default to hide the removal alert after 5 sec
  setTimeout(function(){
  hideRemoveAlert();
  }, 5000); 
  }
  
  function hideRemoveAlert() {
  $(".removeAlert").fadeOut(500);
  }
  
  function addItemBackIn() {
  sum = 0;
  $(removedItem).prependTo("table.items tbody").hide().fadeIn(500) 
  calculatePrices();
  }
  
  function updateSubTotal(){
  $("table.items td.itemTotal").each(function(){
  var value = $(this).text();
  // set the pricePer to a nice, digestable number
  value = formatNum(value);
  
  sum += parseFloat(value);
  $("table.pricing td.subtotal").text("$" + sum.toFixed(2));
  });
  }
  
  function addTax() {
  var tax = parseFloat(sum * 0.05).toFixed(2);
  $("table.pricing td.tax").text("$" + tax);
  }
  
  function calculateTotal() {
  var subtotal = $("table.pricing td.subtotal").text(),
    tax = $("table.pricing td.tax").text(),
    shipping = $("table.pricing td.shipping").text(),
    total;
  
  subtotal = formatNum(subtotal);
  tax = formatNum(tax);
  shipping = formatNum(shipping);
  
  total = (subtotal + tax + shipping).toFixed(2);
  
  $("table.pricing td.orderTotal").text("$" + total);
  }
  
  function calculatePrices() {
  updateSubTotal();
  addTax();
  calculateTotal();
  }
  
  function formatNum(num) {
  return parseFloat(num.replace(/[^0-9-.]/g, ''));
  }