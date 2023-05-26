const date_picker_element = document.querySelector(".date-picker");
const selected_date_element = document.querySelector(
  ".date-picker .selected-date"
);
const selected_time_element = document.querySelector(
  ".time-picker .selected-time"
);
const dates_element = document.querySelector(".date-picker .dates");
const time_slot_element = document.querySelector(".time-picker .time-slot");
const time_picker_element = document.querySelector(".time-picker");
const mth_element = document.querySelector(".date-picker .dates .month .mth");
const next_mth_element = document.querySelector(
  ".date-picker .dates .month .next-mth"
);
const prev_mth_element = document.querySelector(
  ".date-picker .dates .month .prev-mth"
);
const days_element = document.querySelector(".date-picker .dates .days");
const times_element = document.querySelector(".time-picker .time-slot .times");
const s_time_element = document.querySelector(".search_time");
const s_date_element = document.querySelector(".search_date");

const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];
const days_w = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
const times = ["09:00:00", "10:00:00", "11:00:00", "12:00:00", "1:00:00", "2:00:00", "3:00:00"];

//Getting Counter for each month
function cnt_mnth(){
let cnt_list = document.querySelector("#cnt").innerHTML;
count=cnt_list.split("[").join(',').split("]").join(",").split(" ").join(",").split(",,");

}

//Getting Counter for each day
function count_day(){
let counted_list = document.querySelector("#counted").innerHTML;
counted=counted_list.split("[").join(',').split("]").join(",").split(" ").join(",").split(",,").join(",").split(",,").join(",").split(",");
}

//setting date
let date = new Date();
let day = date.getDate();
let month = date.getMonth();
let year = date.getFullYear();
let day_w = date.getDay();

let selectedDate = new Date(year, month + 1, day);
let selectedDay = day;
let selectedMonth = month;
let selectedYear = year;
let selectedDay_w = day_w;
let selectedTime = date.getHours();
if (selectedTime > 12) {
  selectedTime = selectedTime - 12;
}
mth_element.textContent = months[month] + " " + year;
selectedTime++
selected_time_element.value = selectedTime + ":00:00";
selected_date_element.value =
  selectedDate.getDate() +
  "/" +
  selectedDate.getMonth() +
  "/" +
  selectedDate.getFullYear();
selected_date_element.dataset.value = selected_date_element.value;

if (!(selected_time_element.value in times)) {
  selected_time_element.value = "9:00:00";
}

populateDates();
populateTimes();

// EVENT LISTENERS
selected_date_element.addEventListener("click", toggleDatePicker);
selected_time_element.addEventListener("click", toggleTimePicker);
next_mth_element.addEventListener("click", goToNextMonth);
prev_mth_element.addEventListener("click", goToPrevMonth);
s_time_element.addEventListener("click", toggleTimePicker);
s_date_element.addEventListener("click", toggleDatePicker);
s_date_element.addEventListener("click", addTimePicker);

// FUNCTIONS
function toggleTimePicker(e) {
  time_slot_element.classList.toggle("activate");
}
function addTimePicker(e) {
  populateTimes();
  time_picker_element.classList.add("activated");
}
function toggleDatePicker(e) {
  dates_element.classList.toggle("active");
  time_picker_element.classList.remove("activated");

}
function goToNextMonth(e) {
  if (year >= 2023 && month >= 11) {
    next_mth_element.classList.add("disabled");
  } else {
    next_mth_element.classList.remove("disabled");
    month++;
    if (month > 11) {
      month = 0;
      year++;
    }
    mth_element.textContent = months[month] + " " + year;
    populateDates();
    populateTimes();
  }
}

function goToPrevMonth(e) {
  if (year <= 2023 && month <= 0) {
    prev_mth_element.classList.add("disabled");
  } else {
    prev_mth_element.classList.remove("disabled");
    month--;
    if (month < 0) {
      month = 11;
      year--;
    }
    mth_element.textContent = months[month] + " " + year;
    populateDates();
    populateTimes();
  }
}

function populateDates(e) {
  cnt_mnth();
  days_element.innerHTML = "";
  let prevLastDay = new Date(year, month, 0).getDate();
  let firstDayIndex = new Date(year, month).getDay();
  let lastDayIndex = new Date(year, month + 1, 0).getDay();
  let amount_days = new Date(year, month + 1, 0).getDate();
  let nextDays = 6 - lastDayIndex;

  //prev_dates
  for (let x = firstDayIndex; x > 0; x--) {
    const day_element = document.createElement("div");
    day_element.classList.add("day");
    day_element.classList.add("prev_date");
    day_element.textContent = prevLastDay - x + 1;
    days_element.appendChild(day_element);
  }

  //current_dates
  for (let i = 1; i <= amount_days; i++) {
    const day_element = document.createElement("div");
    day_element.classList.add("day");
    day_element.textContent = i;
    if (count[(month*32)+i] <= 2) {
      day_element.classList.add("high_available");
    } else if (count[(month*32)+i] <= 6 && count[(month*32)+i] > 2) {
      day_element.classList.add("med_available");
    } else {
      day_element.classList.add("low_available");
    }

    if (selectedDay == i && selectedYear == year && selectedMonth == month) {
      day_element.classList.add("selected");
    }

    day_element.addEventListener("click", function () {
      selectedDate = new Date(year, month + 1, i);
      selectedDay = i;
      selectedMonth = month;
      selectedYear = year;

      selected_date_element.value =
        selectedDate.getDate() +
        "/" +
        selectedDate.getMonth() +
        "/" +
        selectedDate.getFullYear();
      selected_date_element.dataset.value = selected_date_element.value;
      populateTimes();
      populateDates();
    });
    days_element.appendChild(day_element);
  }

  //next_dates
  for (let y = 1; y <= nextDays; y++) {
    const day_element = document.createElement("div");
    day_element.classList.add("day");
    day_element.classList.add("next_date");
    day_element.textContent = y;
    days_element.appendChild(day_element);
  }
}

function populateTimes(e) {
  count_day();
  times_element.innerHTML = "";
  for (let i = 1; i < 8; i++) {
    const time_element = document.createElement("div");
    time_element.classList.add("time");
    if(counted[(month*31*7)+(((selectedDay-1)*7)+i)]==1){
      time_element.classList.add("already_booked");
    }
    if (selected_time_element.value == times[i-1]) {
      time_element.classList.add("selected");
    }
    time_element.textContent = times[i-1];

    time_element.addEventListener("click", function () {
      selectedTime = time_element.textContent;
      selected_time_element.value = selectedTime;
      selected_time_element.dataset.value = selectedTime;

      populateTimes();
    });

    times_element.appendChild(time_element);
  }
}
