$(function(){
  // setup autocomplete function pulling from allCompanies[] array
  $('#autocomplete').autocomplete({
    lookup: allCompanies,
    onSelect: function (suggestion) {
      document.location = 'findsimilar/'+suggestion.data;
    }
  });
  

});