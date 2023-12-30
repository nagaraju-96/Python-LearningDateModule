# Unit tests for LDate

import unittest
import ldate

class LDateStudentTest(unittest.TestCase):

    #
    # isLeapYear
    #

    def test_a_is_leap_year1(self):
        self.assertTrue(ldate.LDate.is_leap_year(1984))

    def test_a_is_leap_year2(self):
        self.assertFalse(ldate.LDate.is_leap_year(1985))

    # Additional test cases for is_leap_year
    def test_a_is_leap_year3(self):
        self.assertTrue(ldate.LDate.is_leap_year(2000))

    def test_a_is_leap_year4(self):
        self.assertFalse(ldate.LDate.is_leap_year(1900))

    # Additional test cases for is_valid_date
    def test_b_is_valid_date_month_is_13(self):
        self.assertFalse(ldate.LDate.is_valid_date(2022, 13, 7))

    def test_b_is_valid_date_day_is_32(self):
        self.assertFalse(ldate.LDate.is_valid_date(2022, 5, 32))

    #
    # is_valid_date
    #

    def test_b_is_valid_date_month_is_0(self):
        self.assertFalse(ldate.LDate.is_valid_date(2022, 0, 7))

    # Additional test cases for less than
    def test_b_is_valid_date_day_is_negative(self):
        self.assertFalse(ldate.LDate.is_valid_date(2022, 5, -7))

    def test_b_is_valid_date_month_is_negative(self):
        self.assertFalse(ldate.LDate.is_valid_date(2022, -5, 7))

    def test_b_is_valid_date_valid_leap_year(self):
        self.assertTrue(ldate.LDate.is_valid_date(2000, 2, 29))

    def test_b_is_valid_date_invalid_leap_year(self):
        self.assertFalse(ldate.LDate.is_valid_date(1900, 2, 29))

    def test_b_is_valid_date_valid_future_date(self):
        self.assertTrue(ldate.LDate.is_valid_date(2200, 1, 1))

    def test_b_is_valid_date_invalid_future_date(self):
        self.assertFalse(ldate.LDate.is_valid_date(2200, 12, 32))

    def test_b_is_valid_date_valid_past_date(self):
        self.assertTrue(ldate.LDate.is_valid_date(1800, 6, 15))

    def test_b_is_valid_date_valid_date_near_boundary(self):
        self.assertTrue(ldate.LDate.is_valid_date(9999, 12, 31))

    def test_b_is_valid_date_invalid_date_near_boundary(self):
        self.assertFalse(ldate.LDate.is_valid_date(9999, 12, 32))

    #
    # equal
    #
    def test_c_is_equal_1(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 6)
        self.assertTrue(d1 == d2)

    def test_c_is_equal_2(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 6, 5)
        self.assertFalse(d1 == d2) 

    #
    # less than
    #
    # IMPORTANT: You need more of these than you think.
    # Think of all the different combinations of month, day, 
    # and year with respect to <


    def test_d_lt_1(self):
        d1 = ldate.LDate(2022, 5, 5)
        d2 = ldate.LDate(2022, 5, 6)
        self.assertTrue(d1 < d2)

    def test_d_lt_2(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 5)
        self.assertFalse(d1 < d2)

    def test_c_is_equal_3(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 6)
        self.assertFalse(d1 == None)

    def test_c_is_equal_4(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 6)
        self.assertFalse(d1 == "2022-05-06")

    def test_c_is_equal_5(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 6)
        self.assertTrue(d1 == d2)

    def test_c_is_equal_6(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 7)
        self.assertFalse(d1 == d2)

    def test_c_is_equal_7(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 6, 5)
        self.assertFalse(d1 == d2)

    def test_c_is_equal_8(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2023, 5, 6)
        self.assertFalse(d1 == d2)

    def test_c_is_equal_9(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2023, 6, 5)
        self.assertFalse(d1 == d2)

    def test_c_is_equal_10(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 6, 6)
        self.assertFalse(d1 == d2)

    #
    # less than or equal to
    #

    def test_e_le_1(self):
        d1 = ldate.LDate(2022, 5, 5)
        d2 = ldate.LDate(2022, 5, 6)
        self.assertTrue(d1 <= d2)

    def test_e_le_2(self):
        d1 = ldate.LDate(2022, 5, 5)
        d2 = ldate.LDate(2022, 5, 5)
        self.assertTrue(d1 <= d2)

    def test_e_le_3(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 5)
        self.assertFalse(d1 <= d2)

    def test_e_le_4(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 6, 5)
        self.assertTrue(d1 <= d2)

    def test_e_le_5(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2023, 5, 6)
        self.assertTrue(d1 <= d2)

    def test_e_le_6(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2023, 6, 5)
        self.assertTrue(d1 <= d2)

    def test_e_le_7(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 6)
        self.assertTrue(d1 <= d2)

    def test_e_le_8(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 6, 6)
        self.assertTrue(d1 <= d2)

    def test_e_le_9(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 7)
        self.assertTrue(d1 <= d2)

    def test_e_le_10(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 6, 6)
        self.assertTrue(d1 <= d2)

    #
    #  ordinal_date
    #
    
    def test_f_ordinal_date1(self):
        d = ldate.LDate(1997, 1, 1)
        self.assertEqual(1, d.ordinal_date())

    def test_g_ordinal_date2(self):
        d = ldate.LDate(1995, 2, 1)
        self.assertEqual(32, d.ordinal_date())

    def test_f_ordinal_date3(self):
        d = ldate.LDate(2022, 1, 1)
        self.assertEqual(1, d.ordinal_date())

    def test_f_ordinal_date4(self):
        d = ldate.LDate(2022, 6, 15)
        self.assertEqual(166, d.ordinal_date())

    def test_f_ordinal_date5(self):
        d = ldate.LDate(2022, 12, 31)
        self.assertEqual(365, d.ordinal_date())

    def test_f_ordinal_date6(self):
        d = ldate.LDate(2023, 2, 28)
        self.assertEqual(59, d.ordinal_date())

    def test_f_ordinal_date7(self):
        d = ldate.LDate(2023, 5, 1)
        self.assertEqual(121, d.ordinal_date())

    def test_f_ordinal_date8(self):
        d = ldate.LDate(2023, 9, 30)
        self.assertEqual(273, d.ordinal_date())

    def test_f_ordinal_date9(self):
        d = ldate.LDate(2023, 11, 15)
        self.assertEqual(319, d.ordinal_date())

    def test_f_ordinal_date10(self):
        d = ldate.LDate(2024, 2, 29)
        self.assertEqual(60, d.ordinal_date())

    #
    # days_since  
    #
    def test_h_days_since_same_month(self):
        d1 = ldate.LDate(1997, 3, 10)
        d2 = ldate.LDate(1997, 3, 17)
        self.assertEqual(7, d2.days_since(d1))

    def test_g_days_since_next_month(self):
        d1 = ldate.LDate(1997, 3, 10)
        d2 = ldate.LDate(1997, 4, 17)
        self.assertEqual(38, d2.days_since(d1))

    def test_h_days_since_same_day(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 6)
        self.assertEqual(0, d2.days_since(d1))

    def test_h_days_since_same_month(self):
        d1 = ldate.LDate(2022, 5, 10)
        d2 = ldate.LDate(2022, 5, 17)
        self.assertEqual(7, d2.days_since(d1))

    def test_h_days_since_across_months(self):
        d1 = ldate.LDate(2022, 5, 10)
        d2 = ldate.LDate(2022, 6, 5)
        self.assertEqual(26, d2.days_since(d1))


    def test_h_days_since_across_leap_years(self):
        d1 = ldate.LDate(2020, 2, 29)
        d2 = ldate.LDate(2024, 2, 29)
        self.assertEqual(1461, d2.days_since(d1))


    def test_h_days_since_next_month(self):
        d1 = ldate.LDate(2022, 5, 10)
        d2 = ldate.LDate(2022, 6, 5)
        self.assertEqual(26, d2.days_since(d1))


    def test_h_days_since_same_day_different_years(self):
        d1 = ldate.LDate(2022, 5, 10)
        d2 = ldate.LDate(2023, 5, 10)
        self.assertEqual(365, d2.days_since(d1))


    #
    # day_of_week
    #
    def test_i_day_of_week(self):
        d1 = ldate.LDate(2023, 10, 31)
        self.assertEqual('Tuesday', d1.day_of_week())

    def test_i_day_of_week_same_weekday(self):
        d1 = ldate.LDate(2022, 5, 6)  # Friday
        self.assertEqual('Friday', d1.day_of_week())

    def test_i_day_of_week_next_day(self):
        d1 = ldate.LDate(2022, 5, 6)  # Friday
        d2 = ldate.LDate(2022, 5, 7)  # Saturday
        self.assertEqual('Saturday', d2.day_of_week())

    def test_i_day_of_week_across_weeks(self):
        d1 = ldate.LDate(2022, 5, 6)  # Friday
        d2 = ldate.LDate(2022, 5, 13)  # Friday
        self.assertEqual('Friday', d2.day_of_week())

    def test_i_day_of_week_across_months(self):
        d1 = ldate.LDate(2022, 5, 31)  # Tuesday
        d2 = ldate.LDate(2022, 6, 1)   # Wednesday
        self.assertEqual('Wednesday', d2.day_of_week())

    def test_i_day_of_week_across_years(self):
        d1 = ldate.LDate(2022, 12, 31)  # Saturday
        d2 = ldate.LDate(2023, 1, 1)     # Sunday
        self.assertEqual('Sunday', d2.day_of_week())

    def test_i_day_of_week_leap_year(self):
        d1 = ldate.LDate(2020, 2, 29)  # Saturday
        self.assertEqual('Saturday', d1.day_of_week())

    def test_i_day_of_week_random_date1(self):
        d1 = ldate.LDate(2022, 9, 15)  # Thursday
        self.assertEqual('Thursday', d1.day_of_week())

    def test_i_day_of_week_random_date2(self):
        d1 = ldate.LDate(2023, 8, 7)  # Monday
        self.assertEqual('Monday', d1.day_of_week())

    def test_i_day_of_week_random_date3(self):
        d1 = ldate.LDate(2022, 4, 18)  # Monday
        self.assertEqual('Monday', d1.day_of_week())

    def test_i_day_of_week_random_date4(self):
        d1 = ldate.LDate(2023, 11, 22)  # Wednesday
        self.assertEqual('Wednesday', d1.day_of_week())

    #
    # __str__
    #
    def test_j_str1(self):
        d1 = ldate.LDate(2023, 10, 31)
        self.assertEqual('Tuesday, 31 October 2023', d1.__str__())


    def test_j_str_across_months(self):
        d1 = ldate.LDate(2022, 5, 31)
        self.assertEqual('Tuesday, 31 May 2022', d1.__str__())

    def test_j_str_across_years(self):
        d1 = ldate.LDate(2022, 12, 31)
        self.assertEqual('Saturday, 31 December 2022', d1.__str__())

    def test_j_str_leap_year(self):
        d1 = ldate.LDate(2020, 2, 29)
        self.assertEqual('Saturday, 29 February 2020', d1.__str__())

    def test_j_str_random_date1(self):
        d1 = ldate.LDate(2022, 9, 15)
        self.assertEqual('Thursday, 15 September 2022', d1.__str__())

    def test_j_str_random_date2(self):
        d1 = ldate.LDate(2023, 1, 10)
        self.assertEqual('Tuesday, 10 January 2023', d1.__str__())

    def test_j_str_random_date3(self):
        d1 = ldate.LDate(2022, 4, 18)
        self.assertEqual('Monday, 18 April 2022', d1.__str__())

    def test_j_str_random_date4(self):
        d1 = ldate.LDate(2023, 11, 22)
        self.assertEqual('Wednesday, 22 November 2023', d1.__str__())




    #
    # constructor
    #
    def test_k_constructor_raises_on_bad_date1(self):
    
        # verify that the constructor raises ValueError
        # when passed values that do not correspond to 
        # a valid date.
        with self.assertRaises(ValueError):
            ldate.LDate(1997, 5, 32)

    def test_k_constructor_valid_date(self):
        d1 = ldate.LDate(2022, 5, 6)
        self.assertEqual((2022, 5, 6), (d1.year, d1.month, d1.day))

    def test_k_constructor_valid_leap_year(self):
        d1 = ldate.LDate(2000, 2, 29)
        self.assertEqual((2000, 2, 29), (d1.year, d1.month, d1.day))

    def test_k_constructor_valid_future_date(self):
        d1 = ldate.LDate(2100, 1, 1)
        self.assertEqual((2100, 1, 1), (d1.year, d1.month, d1.day))

    def test_k_constructor_invalid_month(self):
        with self.assertRaises(ValueError):
            ldate.LDate(2022, 13, 7)

    def test_k_constructor_invalid_day(self):
        with self.assertRaises(ValueError):
            ldate.LDate(2022, 5, 32)

    def test_k_constructor_negative_year(self):
        with self.assertRaises(ValueError):
            ldate.LDate(-2022, 5, 7)

    def test_k_constructor_invalid_leap_year(self):
        with self.assertRaises(ValueError):
            ldate.LDate(1900, 2, 29)

    def test_k_constructor_invalid_future_date(self):
        with self.assertRaises(ValueError):
            ldate.LDate(2100, 12, 32)


    def test_k_constructor_zero_month(self):
        with self.assertRaises(ValueError):
            ldate.LDate(2022, 0, 7)

if __name__ == '__main__':
    unittest.main(failfast=True)    
