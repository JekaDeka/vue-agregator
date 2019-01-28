<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="">
          Номера
        </div>
        <div class="" v-for="(item,index) in numbers">
          <div class="container">
            <div class="row">
              <div class="col col-sm col lg">
                <input v-model="numbers[index].number" type="text" name="">
              </div>
              <div class="col col-sm col-lg">
                <input type="checkbox" name="" v-model = "numbers[index].multichannel">
                <label for="checkbox">Мультиканальный</label>
              </div>
              <div class="col col-sm col-lg">
                  <button v-on:click="deleteNumber(index)" type="button" name="button">Delete</button>
              </div>
            </div>
          </div>
        </div>
        <div class="">

            <div class="" v-for="(item,index) in NewNumbers">
              <div class="container">
                <div class="row">
                  <div class="col col-sm col lg">
                    <input v-model="new_numbers[index].number" type="text" name="">
                  </div>
                  <div class="col col-sm col-lg">
                    <input type="checkbox" name="" v-model = "new_numbers[index].multichannel">
                    <label for="checkbox">Мультиканальный</label>
                  </div>
                  <div class="col col-sm col-lg">
                      <button v-on:click="deleteNewNumber(index)" type="button" name="button">Delete</button>
                  </div>
                </div>
              </div>
                </div>

          <div class="">
            <button v-on:click="addNumber" type="button" name="button">Add</button>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col col sm col-lg">
        <div class="">
          Режим работы
        </div>
        <div class="">
          По будням
        </div>
        <div class="container">
          <div class="row">
            <div class="col-1 col-sm-1 col-lg-1">
              <div class="">
                C
              </div>
            </div>
            <div class="col-sm col-lg col">
              <div class="">
                <input v-model="work_clock_weekdays_start" type="text" name="" value="">
              </div>
            </div>
            <div class="col-1 col-sm-1 col-lg-1">
              <div class="">
                До
              </div>
            </div>
            <div class="col col-sm col-lg">
              <div class="">
                <input v-model="work_clock_weekdays_end" type="text" name="" value="">
              </div>
            </div>
          </div>
        </div>
        <div class="">
          Суббота
        </div>
        <div class="container">
          <div class="row">
            <div class="col-1 col-sm-1 col-lg-1">
              <div class="">
                C
              </div>
            </div>
            <div class="col-sm col-lg col">
              <div class="">
                <input v-model="work_clock_saturday_start" type="text" name="" value="">
              </div>
            </div>
            <div class="col-1 col-sm-1 col-lg-1">
              <div class="">
                До
              </div>
            </div>
            <div class="col col-sm col-lg">
              <div class="">
                <input v-model="work_clock_saturday_end" type="text" name="" value="">
              </div>
            </div>
          </div>
        </div>
        <div class="">
          Воскресение
        </div>
        <div class="container">
          <div class="row">
            <div class="col-1 col-sm-1 col-lg-1">
              <div class="">
                C
              </div>
            </div>
            <div class="col-sm col-lg col">
              <div class="">
                <input v-model="work_clock_sunday_start" type="text" name="" value="">
              </div>
            </div>
            <div class="col-1 col-sm-1 col-lg-1">
              <div class="">
                До
              </div>
            </div>
            <div class="col col-sm col-lg">
              <div class="">
                <input v-model="work_clock_sunday_end" type="text" name="" value="">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col col-sm col-lg">
        <div class="">
          О себе
        </div>
        <div class="">
          <textarea v-model="comment_time_work" name="name" rows="4" cols="40"></textarea>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="">
            <button v-on:click="Save" type="button" name="button">Save</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      work_clock_weekdays_start: null,
      work_clock_weekdays_end: null,
      work_clock_saturday_start: null,
      work_clock_saturday_end: null,
      work_clock_sunday_start: null,
      work_clock_sunday_end: null,
      comment_time_work: "",
      seen: true,
      numbers: [],
      delete_number: [],
      seen_number: [],
      new_numbers: [],
    }
  },
  methods: {
    Save: function() {

      var master = this.$store.getters.MASTER
      for (var i = 0; i < this.numbers.length; i++) {
        this.$store.dispatch('PUT_NUMBER', this.numbers[i])
      }
      for (i = 0; i < this.delete_number.length; i++) {
        console.log('DELETE' + this.delete_number[i].id)
        this.$store.dispatch('DELETE_NUMBER', this.delete_number[i])
      }
      for (i = 0; i < this.new_numbers.length; i++) {
        this.$store.dispatch("POST_NUMBER", this.new_numbers[i])
      }
      master.work_clock_weekdays_start = this.work_clock_weekdays_start
      master.work_clock_weekdays_end = this.work_clock_weekdays_end
      master.work_clock_saturday_start = this.work_clock_saturday_start
      master.work_clock_saturday_end = this.work_clock_saturday_end
      master.work_clock_sunday_start = this.work_clock_sunday_start
      master.work_clock_sunday_end = this.work_clock_sunday_end
      master.comment_time_work = this.comment_time_work
      this.$store.dispatch('PUT_MASTER', master)
      this.$store.dispatch('GET_NUMBERS_BY_MASTER', master.id)
    },
    deleteNumber: function(index) {

      this.delete_number.push(this.numbers[index])
      console.log(this.delete_number)
      this.numbers.splice(index, 1)


    },
    addNumber: function() {
      var new_number = {
        "number": "",
        "multichannel": false,
        "manufacture": null,
        "master": this.$store.getters.MASTER.id,
      }
      this.new_numbers.push(new_number)
    },
    deleteNewNumber: function(index) {
      this.new_numbers.splice(index, 1)
    },
  },
  computed: {

    NewNumbers: function() {
      return this.new_numbers
    }
  },
  mounted: function() {

    var numbers_obj = this.$store.getters.NUMBERS_BY_MASTER
    this.numbers = numbers_obj
    var master = this.$store.getters.MASTER
    if (master.work_clock_weekdays_start != null)
      this.work_clock_weekdays_start = master.work_clock_weekdays_start
    if (master.work_clock_weekdays_end != null)
      this.work_clock_weekdays_end = master.work_clock_weekdays_end
    if (master.work_clock_saturday_start != null)
      this.work_clock_saturday_start = master.work_clock_saturday_start
    if (master.work_clock_saturday_end != null)
      this.work_clock_saturday_end = master.work_clock_saturday_end
    if (master.work_clock_sunday_start != null)
      this.work_clock_sunday_start = master.work_clock_sunday_start
    if (master.work_clock_sunday_end != null)
      this.work_clock_sunday_end = master.work_clock_sunday_end
    if (master.comment_time_work != null)
      this.comment_time_work = master.comment_time_work
  },
}
</script>

<style lang="css" scoped>
</style>
