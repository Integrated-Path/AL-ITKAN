# -*- coding: utf-8 -*-
from odoo import models, fields, api

"""Added by AhmedNaseem @IntegerEGRATEDPATH in 23/7/2020 , 
AL-ITKAN job Application form adjustment """



class ItkApplForm(models.Model):
    _inherit="hr.applicant"

    SKILL_LEVEL = [("not familiar","Not Familiar"),
                    ("beginner","Beginner"),
                    ("Intermediate","Intermediate"),
                    ("advacned","Advanced"),
                    ("expert","Expert")]


    """ Personal Details """

    surname = fields.Char(string="Surname",required=True)
    address = fields.Char(string="address",required=True)
    hai = fields.Char(string="Hai",required=True)
    sec = fields.Char(string="Sec",required=True)
    st = fields.Char(string="St",required=True)
    house = fields.Char(string="House",required=True)
    Nearest = fields.Char(string="Nearest POR",required=True)
    birthdate = fields.Date(string="Birthdate",required=True)
    place_of_birth = fields.Char(string="Place of Birth",required=True)
    gender = fields.Selection([("male","Male"),("female","Female")],required=True)
    height = fields.Integer(string="Height",required=True)
    weight = fields.Integer(string="Weigh",required=True)
    citizenship = fields.Many2one("res.country")
    religion = fields.Char(string="Religion",required=True)
    social_status=fields.Selection([("single","Single"),
                                    ("enganged","Engaged"),
                                    ("married","Married"),
                                    ("seperated","Seperated"),
                                    ("widowed","Widowed"),
                                    ("divorced","Divorced")],required=True)
    
    """Family Information"""

    father_profession = fields.Char(string="Father`s Profession",required=True)
    mother_profession = fields.Char(string="Mother`s Profession",required=True)
    
    first_name = fields.Char(string="First Name")
    profession = fields.Char(string="Profession")

    first_name_1 = fields.Char(string="First Name")
    profession_1 = fields.Char(string="Profession")

    first_name_2 = fields.Char(string="First Name")
    profession_2 = fields.Char(string="Profession")

    first_name_3 = fields.Char(string="First Name")
    profession_3 = fields.Char(string="Profession")

    first_name_4 = fields.Char(string="First Name")
    profession_4 = fields.Char(string="Profession")

    first_name_5 = fields.Char(string="First Name")
    profession_5 = fields.Char(string="Profession")

    first_name_6 = fields.Char(string="First Name")
    profession_6 = fields.Char(string="Profession")

    first_name_7 = fields.Char(string="First Name")
    profession_7 = fields.Char(string="Profession")
    

    """ Health and Limitations """
    health_status = fields.Selection([("excellent","Excellent"),
                                     ("good","Good"),
                                     ("average","Average"),
                                     ("below average","Below Average"),
                                     ("poor","Poor"),
                                     ("very poor","Very Poor")],required=True,string="Your Health Status?")

    """ Have you suffered or are you suffering from any Terminal Illness or Chronic Disease?"""
    disease = fields.Selection([("yes","YES"),("no","NO")])

    """ Are there any limitations on your ability to perform in your prospective field of work?"""
    limitaions = fields.Selection([("yes","YES"),("no","NO")])

    """Are there any limitations on your ability to engage in all types of travel? Inside or outside Iraq"""
    limitaions_travel = fields.Selection([("yes","YES"),("no","NO")])



    """ Languages and level of Proficiency """
    """ Please Rate your Language Skills on the following scale:
 (1) Excellent (2) Very Good (3) Good (4) Average (5) Below Average (6) Poor (7) Very Poor """
 
    """ Arabic """

    ar_r = fields.Integer(string="")
    ar_w = fields.Integer(string="")
    ar_s = fields.Integer(string="")
    ar_u = fields.Integer(string="")
    ar_o = fields.Integer(string="")

    """ English """

    en_r = fields.Integer(string="")
    en_w = fields.Integer(string="")
    en_s = fields.Integer(string="")
    en_u = fields.Integer(string="")
    en_o = fields.Integer(string="")

    """ Other """

    other_name = fields.Char(string="")
    other_r = fields.Integer(string="")
    other_w = fields.Integer(string="")
    other_s = fields.Integer(string="")
    other_u = fields.Integer(string="")
    other_o = fields.Integer(string="")

    """ Other 1 """

    other_name_1 = fields.Char(string="")
    other_r_1 = fields.Integer(string="")
    other_w_1 = fields.Integer(string="")
    other_s_1 = fields.Integer(string="")
    other_u_1 = fields.Integer(string="")
    other_o_1 = fields.Integer(string="")


    """ Education """
    primary_name = fields.Char(string="Primary",required=True)
    primary_years = fields.Integer(string="# of Years")
    primary_avg = fields.Integer(string="Average(%)")


    Integerermediate_name = fields.Char(string="Integerermediate",required=True)
    Integerermediate_years = fields.Integer(string="# of Years")
    Integerermediate_avg = fields.Integer(string="Average(%)")


    secondary_name = fields.Char(string="Secondary",required=True)
    secondary_years = fields.Integer(string="# of Years")
    secondary_avg = fields.Integer(string="Average(%)")


    college_name = fields.Char(string="College or Institte",required=True)
    college_years = fields.Integer(string="# of Years")
    college_avg = fields.Integer(string="Average(%)")


    other_name = fields.Char(string="Other ",required=True)
    other_years = fields.Integer(string="# of Years")
    other_avg = fields.Integer(string="Average(%)")


    other_1_name = fields.Char(string="Other 1",required=True)
    other_1_years = fields.Integer(string="# of Years")
    other_1_avg = fields.Integer(string="Average(%)")


    highest_acad = fields.Char(string="Highest Academic Qalification")
    highest_grad_year = fields.Integer(string="Graduation Year")
    highest_uni = fields.Char(string="University")
    highest_country = fields.Char(string="Country")


    """ Referral Info """
    referral_source = fields.Selection([("walk-in","Walk-In"),
                                        ("employee","Employee"),
                                        ("facebook","Facebook"),
                                        ("linked-in","Linked-In")])

    other_referral_source =fields.Char(string="Other Referral Source")

    preffered_fow = fields.Selection([("technical","Technical"),
                                    ("sales","Sales"),
                                    ("administration","Administration")])
    
    preferred_cp = fields.Selection([("3 years","3 Years"),
                                    ("5 years","5 Years"),
                                    ("10 years","10 Years")])

    """ Technical Skills """

    skill_1_Desc = fields.Char(string="")
    skill_1_level = fields.Selection(SKILL_LEVEL)

    skill_2_Desc = fields.Char(string="")
    skill_2_level = fields.Selection(SKILL_LEVEL)

    skill_3_Desc = fields.Char(string="")
    skill_3_level = fields.Selection(SKILL_LEVEL)
    

    skill_4_Desc = fields.Char(string="")
    skill_4_level = fields.Selection(SKILL_LEVEL)                                    


    skill_5_Desc = fields.Char(string="")
    skill_5_level = fields.Selection(SKILL_LEVEL)


    skill_6_Desc = fields.Char(string="")
    skill_6_level = fields.Selection(SKILL_LEVEL)



    skill_7_Desc = fields.Char(string="")
    skill_7_level = fields.Selection(SKILL_LEVEL)


    skill_8_Desc = fields.Char(string="")
    skill_8_level = fields.Selection(SKILL_LEVEL)

    
    
    """ Administration Skills """

    business_correspondence_skill_level = fields.Selection(SKILL_LEVEL)
    effective_communication_skill_level = fields.Selection(SKILL_LEVEL)
    customer_service_skill_level = fields.Selection(SKILL_LEVEL)
    team_work_skill_level = fields.Selection(SKILL_LEVEL)
    Integerernet_and_research_skill_level = fields.Selection(SKILL_LEVEL)
    ms_office_and_outlook_skill_level = fields.Selection(SKILL_LEVEL)
    office_machine_skill_level = fields.Selection(SKILL_LEVEL)
    typing_skill_level = fields.Selection(SKILL_LEVEL)
    time_management_skill_level = fields.Selection(SKILL_LEVEL)
    attention_to_detail_level = fields.Selection(SKILL_LEVEL)
    goal_oriented_skill_level = fields.Selection(SKILL_LEVEL)
    multi_tasking_skill_level = fields.Selection(SKILL_LEVEL)
    follow_up_skill_level = fields.Selection(SKILL_LEVEL)
    employee_relation_skill_level = fields.Selection(SKILL_LEVEL)
    supervision_skill_level = fields.Selection(SKILL_LEVEL)

    """ Sales Skills """

    relationship_building_skill_level= fields.Selection(SKILL_LEVEL)
    time_management_skill_level= fields.Selection(SKILL_LEVEL)
    research_information_gathering_skill_level= fields.Selection(SKILL_LEVEL)
    medical_product_knowledge_skill_level= fields.Selection(SKILL_LEVEL)
    business_communication_skill_level= fields.Selection(SKILL_LEVEL)
    client_engagement_skill_level= fields.Selection(SKILL_LEVEL)
    sales_presentations_demos_skill_level= fields.Selection(SKILL_LEVEL)
    contract_negotiation_skill_level= fields.Selection(SKILL_LEVEL)
    closing_skills_skill_level= fields.Selection(SKILL_LEVEL)
    self_motivated_ambitious_skill_level= fields.Selection(SKILL_LEVEL)
    adaptability_skill_level= fields.Selection(SKILL_LEVEL)
    responsibility_skill_level= fields.Selection(SKILL_LEVEL)
    goal_oriented_skill_level= fields.Selection(SKILL_LEVEL)
    passionate_about_selling_skill_level= fields.Selection(SKILL_LEVEL)



    "Training and Certifications"

    t1 = fields.Char(string="")
    t1_year = fields.Integer(string="")
    t1_awarded_by = fields.Char(string="")
    t1_country_city = fields.Char(string="")

    t2 = fields.Char(string="")
    t2_year = fields.Integer(string="")
    t2_awarded_by = fields.Char(string="")
    t2_country_city = fields.Char(string="")

    t3 = fields.Char(string="")
    t3_year = fields.Integer(string="")
    t3_awarded_by = fields.Char(string="")
    t3_country_city = fields.Char(string="")

    t4 = fields.Char(string="")
    t4_year = fields.Integer(string="")
    t4_awarded_by = fields.Char(string="")
    t4_country_city = fields.Char(string="")

    t5 = fields.Char(string="")
    t5_year = fields.Integer(string="")
    t5_awarded_by = fields.Char(string="")
    t5_country_city = fields.Char(string="")

    t6 = fields.Char(string="")
    t6_year = fields.Integer(string="")
    t6_awarded_by = fields.Char(string="")
    t6_country_city = fields.Char(string="")

    t7 = fields.Char(string="")
    t7_year = fields.Integer(string="")
    t7_awarded_by = fields.Char(string="")
    t7_country_city = fields.Char(string="")

    """ Employment History """

    contact_disclaimer = fields.Boolean(string="")

    employer_name = fields.Char(string="")
    job_title = fields.Char(string="")
    employer_address = fields.Char(string="")
    employer_province = fields.Char(string="")
    from_date = fields.Date(string="Date")
    to_date = fields.Date(string="Date")
    starting_slry = fields.Integer()
    ending_slry = fields.Integer()
    supervisor = fields.Char(string="")
    super_phone = fields.Char(string="")
    reason_for_leaving = fields.Char(string="")



    employer_name_1 = fields.Char(string="")
    job_title_1 = fields.Char(string="")
    employer_address_1 = fields.Char(string="")
    employer_province_1 = fields.Char(string="")
    from_date_1 = fields.Date(string="Date")
    to_date_1 = fields.Date(string="Date")
    starting_slry_1 = fields.Integer()
    ending_slry_1 = fields.Integer()
    supervisor_1 = fields.Char(string="")
    super_phone_1 = fields.Char(string="")
    reason_for_leaving_1 = fields.Char(string="")




    employer_name_2 = fields.Char(string="")
    job_title_2 = fields.Char(string="")
    employer_address_2 = fields.Char(string="")
    employer_province_2 = fields.Char(string="")
    from_date_2 = fields.Date(string="Date")
    to_date_2 = fields.Date(string="Date")
    starting_slry_2 = fields.Integer()
    ending_slry_2 = fields.Integer()
    supervisor_2 = fields.Char(string="")
    super_phone_2 = fields.Char(string="")
    reason_for_leaving_2 = fields.Char(string="")


    """ Additional Information """
    union_member = fields.Selection([("yes","YES"),("no","NO")])
    driver_license = fields.Selection([("yes","YES"),("no","NO")])
    driver_license_date = fields.Date(string="Date")
    means_of_transport = fields.Char(string="")
    good_appoint = fields.Selection([("yes","YES"),("no","NO")])
    smoking =fields.Selection([("yes","YES"),("no","NO")])
    long_hours =fields.Selection([("yes","YES"),("no","NO")])
    start_date = fields.Date(string="Date")
    planning_to_study = fields.Selection([("yes","YES"),("no","NO")])
    presently_employed = fields.Selection([("yes","YES"),("no","NO")])
    contact_employer = fields.Selection([("yes","YES"),("no","NO")])


    "Skills 2"
    SKILLS_SET_2 = [("excellent","Excellent"),
                    ("very good","Very Good"),
                    ("good","Good"),
                    ("average","Average"),
                    ("below average","Below Average"),
                    ("poor","Poor"),
                    ("very poor","Very Poor")]

    team_work = fields.Selection(SKILLS_SET_2)
    pressure = fields.Selection(SKILLS_SET_2)
    travel = fields.Selection(SKILLS_SET_2)


    """ references non relatives  """

    ref_name = fields.Char(string="")
    ref_realtion = fields.Char(string="")
    ref_phone = fields.Char(string="")

    ref_name_1 = fields.Char(string="")
    ref_realtion_1 = fields.Char(string="")
    ref_phone_1 = fields.Char(string="")

    """ refrences Relatives """

    ref_r_name = fields.Char(string="")
    ref_r_realtion = fields.Char(string="")
    ref_r_phone = fields.Char(string="")

    ref_r_name_1 = fields.Char(string="")
    ref_r_realtion_1 = fields.Char(string="")
    ref_r_phone_1 = fields.Char(string="")


    """ Signature """
    signature = fields.Char(string="")
    Date = fields.Date(string="Date")



    """ Supporting Documents """
    national_id = fields.Binary()
    citizenship_cert = fields.Binary()
    accomodation_id = fields.Binary()
    uni_degree = fields.Binary()
    medical = fields.Binary()
    no_crim_req = fields.Binary()
    letter_rec_1 = fields.Binary()
    letter_rec_2 = fields.Binary()





    

