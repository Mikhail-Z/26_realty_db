function render_template(text, ad_info) {
    text = text.replace(/{rooms_number}/g, ad_info.rooms_number)
        .replace(/{price}/g, ad_info.price)
        .replace(/{settlement}/g, ad_info.settlement)
        .replace(/{address}/g, ad_info.address)
        .replace(/{premise_area}/g, ad_info.premise_area)
    return text
}
var insert2page = (ad_info) => {
    var container = document.getElementById('ad_template');
    var containerContent = container.textContent || container.innerText;
    console.log(containerContent)
    renderedContent = render_template(containerContent, ad_info);
    $("#ads_list").append(renderedContent)
}



var update_pagination = (page, cur_page, next_url, pages_num, prev_url) => {
  var pagination_root = $('<div class="panel-body"><div class="clearfix text-center"><ul class="pagination"></ul></div></div>')
  var next_page_btn

  if (prev_url)
    prev_page_btn = `<li><a href="${prev_url}"><span>«</span></a></li>`
  else
    prev_page_btn = `<li class="disabled"><a href="${prev_url}"><span>«</span></a></li>`
  if (next_url)
    next_page_btn = `<li><a href="${next_url}"><span>&raquo;</span></a></li>`
  else
    next_page_btn = `<li class="disabled"><a href="${next_url}"><span>&raquo;</span></a></li>`

  var pagination_content = prev_page_btn
  for (page = 1; page < pages_num + 1; page++) {
    let page_ptr;
    if (page === cur_page)
      page_ptr = `<li class="active"><span>${page}<span class="sr-only">(current)</span></span></li>`
    else
      page_ptr = `<li><a href="?page=${page}">${page}</a></li>`
    pagination_content += page_ptr
  }
  pagination_content += next_page_btn
  pagination_root.find("ul.pagination").append(pagination_content)
  $("#ads_list").append(pagination_root)
}

    var update_ads_list = (ads, pages_num) => {
      var ads_list_elem = $("#ads_list")
      ads_list_elem.empty()
      if (pages_num > 0) {
        for (i = 0; i < ads.length; i++) {
          insert2page(ads[i])
        }
      } else {
        ads_list_elem.append("<div class='panel-body'><h3>К сожалению, по таким параметрам объявлений нет.</h3></div>")
      }

    }


    var search_ads = (url) => {
      var form = $(document).find("[name='ads_filter']")
      var oblast_district = form.find("select[name='oblast_district']").val()

      var min_price = form.find("[name='min_price']").val()
      var max_price = form.find("[name='max_price']").val()

      var formData = {oblast_district}

      if (form.find("[name='new_building']:checked").length > 0) {
        formData.new_building = true
      }
      if (min_price !== "")
        formData.min_price = min_price
      if (max_price !== "")
        formData.max_price = max_price

      $.ajax({
        method: "GET",
        url: url,
        data: formData,
        success: (json) => {
          update_ads_list(json["ads"], json["pages_num"])
          if (json["pages_num"] > 0) {
            update_pagination(
                json["page"], json["cur_page"], json["next_url"], json["pages_num"], json["prev_url"]
              )
          }
        }
      })
    }

    // click on page pointer or filter button
    $(document).on("click", "#show_ads, ul.pagination", function(event) {
      event.preventDefault()
      if ($(event.target).is("button"))
        search_ads("/")
      else if ($(event.target).is("a") && $(event.target).parents(".disabled").length === 0) {
        //click was on page button, but not on text in it
        let url = $(event.target).attr("href")
        search_ads(url)
      } else if ($(event.target).parent().is("a") && $(event.target).parents(".disabled").length === 0) {
        //click was on page button on text in it
        let url = $(event.target).parent().attr("href")
        search_ads(url)
      }
    })
