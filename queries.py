select_keywords = '''
    select id, name 
    from keyword 
    WHERE use=true 
    order by name;
'''

select_images = '''
    select id, 
        name, 
        SPLIT_PART(file, '/', 6) as original_label
    from cad_file 
    where label = {label} and file like '%%.obj' {cad_type}
    order by file_size, name;
'''

select_category = '''
    select id, name 
    from keyword 
    where use = True and parent={parent}
    order by name;
'''

update_label = '''
    update cad_file set label='{label}' where id='{id}';
'''

select_object_by_id = '''
    select * from cad_file where id='{id}';
'''

stats = '''
    SELECT B.name as Category, A.SubCategory, A.ME444, A.Data_Warehouse, A.grabCAD, A.TOTAL
    FROM (SELECT CASE WHEN keyword.parent = 0 THEN keyword.id ELSE keyword.parent END as Category,
                 keyword.name                                                         as SubCategory,
                 SUM(CASE WHEN source = 1 THEN 1 ELSE 0 END)                          as ME444,
                 SUM(CASE WHEN source = 2 THEN 1 ELSE 0 END)                          as Data_Warehouse,
                 SUM(CASE WHEN source = 3 THEN 1 ELSE 0 END)                          as grabCAD,
                 COUNT(*)                                                             as TOTAL
          FROM cad_file
          LEFT JOIN keyword
          ON cad_file.label = keyword.id
          WHERE file like '%%.obj'
            and label >= 0
            and use = true
          GROUP BY keyword.id
          ORDER BY Category ASC
         ) AS A
    LEFT JOIN keyword B
    ON A.Category = B.id
    ORDER BY A.Category
'''

select_unlabeled = '''
    SELECT id,
           name,
           SPLIT_PART(file, '/', 6) as original_label
    FROM cad_file
    WHERE label = ''
    ORDER BY name;
'''


