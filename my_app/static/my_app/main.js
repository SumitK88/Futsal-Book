
const date_picker_element = document.querySelector('.date-picker');
const selected_date_element = document.querySelector('.date-picker .selected-date');
const dates_element = document.querySelector('.date-picker .dates');
const time_picker_element = document.querySelector('.time-picker');
const mth_element = document.querySelector('.date-picker .dates .month .mth');
const next_mth_element = document.querySelector('.date-picker .dates .month .next-mth');
const prev_mth_element = document.querySelector('.date-picker .dates .month .prev-mth');
const days_element = document.querySelector('.date-picker .dates .days');
const time_element = document.querySelector('.search_time');
const times_element = document.querySelector('.time_slot');

const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const days_w = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const times = ['09:00', '10:00', '11:00', '12:00', '1:00', '2:00', '3:00']
//Getting Counter for each month
let cnt_list = document.querySelector('#cnt').innerHTML;
let num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], cr = 0, c = [], count = [];
for (let i = 0; i < 1141; i++) {
    cl = cnt_list[i];
    if (cl in num) {
        if (cr > 30) {
            cr = cr - 31;
            count.push(c);
            c = [];
            c.push(cl);
        }
        else {
            c.push(cl);
        }
        cr++;
    }
};
count.push(c);

//Getting Counter for each day
let cnt_d_list = document.querySelector('#cnt_d').innerHTML;
let num_d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], cr_d = 0, c_d = [], count_d = [];
for (let i = 0; i < 1141; i++) {
    let cl_d = cnt_d_list[i];
    if (cl_d in num) {
        if (cr_d > 30) {
            cr_d = cr_d - 31;
            count.push(c_d);
            c_d = [];
            c_d.push(cl_d);
        }
        else {
            c_d.push(cl_d);
        }
        cr_d++;
    }
};
count.push(c_d);


//setting date 
let date = new Date();
let day = date.getDate();
let month = date.getMonth();
let year = date.getFullYear();
let day_w = date.getDay();

let selectedDate = date;
let selectedDay = day;
let selectedMonth = month;
let selectedYear = year;
let selectedDay_w = day_w;

mth_element.textContent = months[month] + ' ' + year;

selected_date_element.textContent = date.toDateString();
selected_date_element.dataset.value = selectedDate;

populateDates();
populateTimes();

// EVENT LISTENERS
selected_date_element.addEventListener('click', toggleDatePicker);
next_mth_element.addEventListener('click', goToNextMonth);
prev_mth_element.addEventListener('click', goToPrevMonth);
time_element.addEventListener('click', toggleTimePicker);
time_element.addEventListener('click', toggleDatePicker);

// FUNCTIONS
function toggleTimePicker(e) {
    times_element.classList.add('active');
}
function toggleDatePicker(e) {
    dates_element.classList.toggle('active');
}
function goToNextMonth(e) {
    if (year >= 2023 && month >= 11) {
        next_mth_element.classList.add('disabled');
    } else {
        next_mth_element.classList.remove('disabled');
        month++;
        if (month > 11) {
            month = 0;
            year++;
        }
        mth_element.textContent = months[month] + ' ' + year;
        populateDates();
    }
}

function goToPrevMonth(e) {
    if (year <= 2023 && month <= 0) {
        prev_mth_element.classList.add('disabled');
    } else {
        prev_mth_element.classList.remove('disabled');
        month--;
        if (month < 0) {
            month = 11;
            year--;
        }
        mth_element.textContent = months[month] + ' ' + year;
        populateDates();
    }
}

function populateDates(e) {
    days_element.innerHTML = '';
    let prevLastDay = new Date(year, month, 0).getDate();
    let firstDayIndex = new Date(year, month).getDay();
    let lastDayIndex = new Date(year, month + 1, 0).getDay();
    let amount_days = new Date(year, month + 1, 0).getDate();
    let nextDays = 6 - lastDayIndex;
    console.log(firstDayIndex, prevLastDay);

    //prev_dates
    for (let x = firstDayIndex; x > 0; x--) {
        const day_element = document.createElement('div');
        day_element.classList.add('day');
        day_element.classList.add('prev_date');
        day_element.textContent = prevLastDay - x + 1;
        days_element.appendChild(day_element);
    }

    //current_dates
    for (let i = 1; i <= amount_days; i++) {
        const day_element = document.createElement('div');
        day_element.classList.add('day');
        day_element.textContent = i;

        if (count[month][i - 1] <= 2) {
            day_element.classList.add('high_available');
        }
        else if (count[month][i - 1] <= 4 && count[month][i - 1] > 2) {
            day_element.classList.add('med_available');
        }
        else {
            day_element.classList.add('low_available');
        }

        if (selectedDay == (i) && selectedYear == year && selectedMonth == month) {
            day_element.classList.add('selected');
        }

        day_element.addEventListener('click', function () {
            selectedDate = new Date(year + '-' + (month + 1) + '-' + (i));
            selectedDay = (i);
            selectedMonth = month;
            selectedYear = year;

            selected_date_element.textContent = selectedDate.toDateString();;
            selected_date_element.dataset.value = selectedDate;

            populateDates();
        });

        days_element.appendChild(day_element);
    }

    //next_dates
    for (let y = 1; y <= nextDays; y++) {
        const day_element = document.createElement('div');
        day_element.classList.add('day');
        day_element.classList.add('next_date');
        day_element.textContent = y;
        days_element.appendChild(day_element);
    }

}

function populateTimes(e) {
    times_element.innerHTML = '';
    for (let i = 0; i < 6; i++) {
        const time_element = document.createElement('span');
        time_element.classList.add('time');
        time_element.classList.add('next_date');
        time_element.textContent = times[i];
        times_element.appendChild(time_element);
    }
}
